"""Measure wall time, CPU time and peak memory of each public example check.

Run from the repository root: python3 examples/check_resource_use.py
Method: each script runs RUNS times in a child interpreter via runpy; os.wait4
returns that child's CPU time. Wall time includes interpreter start-up. Peak
memory is reported by the child itself: VmHWM on Linux, ru_maxrss on macOS.
Limits below are smoke thresholds for this CI job, not requirements of any
edge device.
"""

import os
import platform
import statistics
import subprocess
import sys
import time
from pathlib import Path

RUNS = 5
WALL_LIMIT_S = 5.0
RSS_LIMIT_KIB = 100 * 1024

# On Linux the parent's ru_maxrss survives into a spawned child across exec, so the
# child reads its own per-process high-water mark instead.
CHILD = """
import runpy, sys
runpy.run_path(sys.argv[1], run_name="__main__")
if sys.platform == "linux":
    kib = next(int(l.split()[1]) for l in open("/proc/self/status") if l.startswith("VmHWM:"))
else:
    import resource
    kib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1024  # macOS reports bytes
print(kib)
"""

HERE = Path(__file__).resolve().parent
SCRIPTS = sorted(p for p in HERE.glob("check_*.py") if p.name != Path(__file__).name)
SCRIPTS.append(HERE / "equilibrium_demo.py")


def run_once(script):
    start = time.perf_counter()
    child = subprocess.Popen([sys.executable, "-c", CHILD, str(script)], cwd=HERE, stdout=subprocess.PIPE)
    out = child.stdout.read()
    child.stdout.close()
    _, status, usage = os.wait4(child.pid, 0)
    wall = time.perf_counter() - start
    child.returncode = os.waitstatus_to_exitcode(status)
    assert child.returncode == 0, f"{script.name} exited {child.returncode}"
    return wall, usage.ru_utime + usage.ru_stime, int(out.split()[-1])


def main():
    lines = [
        f"Python {platform.python_version()} on {platform.platform()}, {os.cpu_count()} CPUs, {RUNS} runs each",
        "",
        "| Script | Median wall (ms) | Median CPU (ms) | Peak RSS (KiB) |",
        "|---|---:|---:|---:|",
    ]
    for script in SCRIPTS:
        runs = [run_once(script) for _ in range(RUNS)]
        wall = statistics.median(r[0] for r in runs)
        cpu = statistics.median(r[1] for r in runs)
        rss = max(r[2] for r in runs)
        assert wall < WALL_LIMIT_S, f"{script.name} median wall {wall:.2f} s"
        assert rss < RSS_LIMIT_KIB, f"{script.name} peak RSS {rss} KiB"
        lines.append(f"| {script.name} | {wall * 1000:.0f} | {cpu * 1000:.0f} | {rss} |")
    report = "\n".join(lines)
    print(report)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as out:
            out.write("## Resource use of public example checks\n\n" + report + "\n")


if __name__ == "__main__":
    main()

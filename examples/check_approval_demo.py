"""Run with python3 examples/check_approval_demo.py."""

from approval_demo import Approval

actions = []
denied = Approval(lambda: actions.append("unexpected"))
assert denied.resolve(False) == "denied" and actions == []
try:
    denied.resolve(True)
except ValueError:
    pass
else:
    raise AssertionError("a resolved request was accepted again")
try:
    Approval(lambda: actions.append("unexpected")).resolve("yes")
except ValueError:
    pass
else:
    raise AssertionError("a non-boolean approval was accepted")
assert actions == []
approved = Approval(lambda: actions.append("done"))
assert approved.resolve(True) == "approved" and actions == ["done"]
print("Synthetic approval checks passed")

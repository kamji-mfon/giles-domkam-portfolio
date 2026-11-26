"""Synthetic statics illustration, not an engineering design or code check."""


def reactions(load):
    if isinstance(load, bool) or not isinstance(load, (int, float)) or not 0 <= load < float("inf"):
        raise ValueError("load must be a finite non-negative number")
    return load / 2, load / 2


if __name__ == "__main__":
    load = 10  # Fictional point load at midspan; force units are consistent.
    left, right = reactions(load)
    assert left + right == load
    for bad in (-1, float("inf"), True, "10"):
        try:
            reactions(bad)
        except ValueError:
            continue
        raise AssertionError(f"invalid load accepted: {bad!r}")
    print(f"Synthetic load: {load}; reactions: {left}, {right}; equilibrium: {left + right == load}")

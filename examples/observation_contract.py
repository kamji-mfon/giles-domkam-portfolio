"""Synthetic authorization example. Does not connect to or authorize equipment."""

from ipaddress import ip_address, ip_network


def permitted(record, target, now):
    """Fail closed unless an explicit scope and validity interval cover the request."""
    if not isinstance(record, dict) or isinstance(now, bool) or not isinstance(now, int):
        return False
    start, end = record.get("start"), record.get("end")
    if any(isinstance(x, bool) or not isinstance(x, int) for x in (start, end)):
        return False
    if not start <= now <= end:
        return False
    scope = record.get("scope")
    if not isinstance(scope, list) or not scope or not isinstance(target, str):
        return False
    try:
        address = ip_address(target)
        networks = [ip_network(entry, strict=True) for entry in scope]
    except (ValueError, TypeError):
        return False
    return any(address in network for network in networks)


if __name__ == "__main__":
    example = {"start": 10, "end": 20, "scope": ["192.0.2.0/24"]}
    print("in scope:", permitted(example, "192.0.2.5", 15))
    print("outside scope:", permitted(example, "198.51.100.5", 15))
    print("expired:", permitted(example, "192.0.2.5", 21))

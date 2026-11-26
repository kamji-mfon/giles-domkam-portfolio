"""Illustrative single-use approval; the action only appends to an in-memory list."""


class Approval:
    def __init__(self, action):
        self.action = action
        self.resolved = False

    def resolve(self, approved):
        if self.resolved:
            raise ValueError("approval already resolved")
        if not isinstance(approved, bool):
            raise ValueError("approval must be a boolean")
        self.resolved = True
        if approved:
            self.action()
            return "approved"
        return "denied"


if __name__ == "__main__":
    actions = []
    request = Approval(lambda: actions.append("synthetic action"))
    print("Decision:", request.resolve(False))
    print("Actions performed:", actions)

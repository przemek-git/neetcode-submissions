class MinStack:
    def __init__(self):
        self.smallest, self.stack = [], []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.smallest and self.smallest[-1] >= val:
            self.smallest.append(val)
        elif not self.smallest:
            self.smallest.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.smallest[-1]:
                self.smallest.pop()
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest[-1] if self.smallest else 0

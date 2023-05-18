class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if len(self.min_stack) > 0 else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    inst = MinStack()
    inst.push(1)
    inst.push(2)
    inst.push(3)
    print(inst.top())  # 3
    print(inst.getMin())  # 1

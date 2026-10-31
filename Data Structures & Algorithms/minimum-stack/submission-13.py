class MinStack:

    def __init__(self):
        self.stk = []
        self.minstk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.minstk:
            self.minstk.append(val)
        elif self.minstk and val <= self.minstk[-1]:
            self.minstk.append(val)

    def pop(self) -> None:
        val = self.stk.pop()
        if val == self.minstk[-1]:
            self.minstk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minstk[-1]

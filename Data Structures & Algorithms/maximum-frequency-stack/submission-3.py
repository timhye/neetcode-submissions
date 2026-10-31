class FreqStack:

    def __init__(self):
        self.store = defaultdict(int)
        self.stk = defaultdict(list)
        self.mfeq = 0

    def push(self, val: int) -> None:
        self.store[val] += 1
        if not self.stk[self.store[val]]:
            self.mfeq = self.store[val] 
        self.stk[self.store[val]].append(val)

    def pop(self) -> int:
        res = self.stk[mfeq].pop()
        if not self.stk[mfeq]:
            self.mfeq -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
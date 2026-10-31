class MyQueue:

    def __init__(self):
        self.pri = []
        self.sec = []

    def push(self, x: int) -> None:
        self.pri.append(x)
        

    def pop(self) -> int:
        if not self.pri:
            return 0
        while len(self.pri) != 1:
            self.sec.append(self.pri.pop())
        
        ans = self.pri.pop()
        while self.sec:
            self.pri.append(self.sec.pop())
        return ans
        

    def peek(self) -> int:
        if not self.pri:
            return 0
        while len(self.pri) != 1:
            self.sec.append(self.pri.pop())
        
        ans = self.pri[-1]
        while self.sec:
            self.pri.append(self.sec.pop())
        return ans
        

        

    def empty(self) -> bool:
        return len(self.pri) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
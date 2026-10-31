class MyStack:

    def __init__(self):
        self.main = deque([])
        self.helper = deque([])

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        while len(self.main) != 1:
            self.helper.append(self.main.popleft())
        
        self.main.popleft()
        self.main, self.helper = self.helper, self.main
        

    def top(self) -> int:
        while len(self.main) != 1:
            self.helper.append(self.main.popleft())
        
        val = self.main[0]
        self.helper.append(self.main.popleft())
        self.main, self.helper = self.helper, self.main
        return val
        

        

    def empty(self) -> bool:
        return len(self.main) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
class MyQueue:

    def __init__(self):
        self.incoming = []
        self.leave = []

    def push(self, x: int) -> None:
        self.incoming.append(x)
        

    def pop(self) -> int:
        if not self.leave and not self.incoming:
            return 0
        elif not self.leave:
            while self.incoming:
                self.leave.append(self.incoming.pop())
        
        return self.leave.pop()
       
        

    def peek(self) -> int:
        print(self.incoming, self.leave)
        if not self.incoming and not self.leave:
            return 0
        elif not self.leave:
            while self.incoming:
                self.leave.append(self.incoming.pop())
    
        return self.leave[-1]
        

        

    def empty(self) -> bool:
        return len(self.leave) == 0 and len(self.incoming) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
class MinStack:

    def __init__(self):
        record = []
    def push(self, val: int) -> None:
        self.record.append(val)
        
    def pop(self) -> None:
        self.record.pop()


    def top(self) -> int:
        return self.record[-1]
        

    def getMin(self) -> int:
        return min(self.record)

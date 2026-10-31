class MinStack:

    def __init__(self):
        record = []
    def push(self, val: int) -> None:
        record.append(val)
        
    def pop(self) -> None:
        record.pop()


    def top(self) -> int:
        return record[-1]
        

    def getMin(self) -> int:
        return min(record)

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        
        if self.store[key] == []:
            return ""
        else:
            right = len(self.store[key]) - 1
            left = 0
            tbr = len(self.store[key])
            while left <= right:
                mid = left + (right - left) // 2
                if self.store[key][mid][1] == timestamp:
                    return self.store[key][mid][0]
                elif self.store[key][mid][1] > timestamp:
                    right = mid - 1
                else:
                    tbr = mid
                    left = mid + 1
            
            if tbr == len(self.store[key]):
                return ""
            else:
                return self.store[key][tbr][0]

                
        

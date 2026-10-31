class MyHashMap:

    def __init__(self):
        self.record = [1000001] * 64

    def put(self, key: int, value: int) -> None:
        if key < len(self.record):
            self.record[key] = value
        else:            
            self.newrecord = [0] * 128
            while len(self.newrecord) <= key:
                self.newrecord *= 2
            
            self.newrecord[key] = value
            for i in range(len(self.record)):
                self.newrecord[i] = self.record[i]
            
            self.record[:] = self.newrecord



                

    def get(self, key: int) -> int:
        if key >= len(self.record):
            return -1
        else:
            if self.record[key] == 1000001:
                return -1
            else:
                return self.record[key]

        

    def remove(self, key: int) -> None:
        if key >= len(self.record):
            return
        else:
            self.record[key] = 1000001
            self.get(key)
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
class MyHashMap:

    def __init__(self):
        self.values = []
        self.keys = set()

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.keys.add(key)
            self.values.append([key,value])
            return
        for i in range(len(self.values)):
            k, v = self.values[i]
            if k == key:
                self.values[i][1] = value
                return

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        for i in range(len(self.values)):
            k, v = self.values[i]
            if k == key:
                return v

    def remove(self, key: int) -> None:
        if key not in self.keys:
            return
        self.keys.remove(key)
        for i in range(len(self.values)):
            k,v = self.values[i]
            if k == key:
                self.values.pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
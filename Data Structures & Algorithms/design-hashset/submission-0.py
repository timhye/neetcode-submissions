class MyHashSet:

    def __init__(self):
        self.record = {key:() for key in range(128)}

    def add(self, key: int) -> None:
        newkey = key % 128
        self.record[newkey].add(key)

    def remove(self, key: int) -> None:
        newkey = key % 128
        self.record[newkey].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.record[key % 128]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
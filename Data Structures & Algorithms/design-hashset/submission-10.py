class MyHashSet:

    def __init__(self):
        self.record = [[] for i in range(128)]

    def add(self, key: int) -> None:
        hashed = key % 128
        if key not in self.record[hashed]:
            self.record[hashed].append(key)

    def remove(self, key: int) -> None:
        hashed = key % 128
        if key in self.record[hashed]:

            self.record[hashed].remove(key)

    def contains(self, key: int) -> bool:
        hashed = key % 128
        return key in self.record[hashed]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
class MyHashSet:

    def __init__(self):
        self.record = [set() for i in range(128)]

    def add(self, key: int) -> None:
        hashed = key % 128
        self.record[hashed].add(key)

    def remove(self, key: int) -> None:
        hashed = key % 128
        self.record[hashed].discard(key)

    def contains(self, key: int) -> bool:
        hashed = key % 128
        return key in self.record[hashed]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
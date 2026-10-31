class LRUCache:
    class Node:
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.mapper = {}
        self.head = None  # LRU
        self.tail = None  # MRU

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev = None
        node.next = None

    def add_to_tail(self, node):
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def put(self, key: int, value: int) -> None:
        if key in self.mapper:
            cur = self.mapper[key]
            cur.value = value
            self.remove(cur)
            self.add_to_tail(cur)
            return

        node = LRUCache.Node(key, value)
        self.mapper[key] = node
        self.add_to_tail(node)
        self.size += 1

        if self.size > self.capacity:
            lru = self.head
            self.remove(lru)
            del self.mapper[lru.key]
            self.size -= 1
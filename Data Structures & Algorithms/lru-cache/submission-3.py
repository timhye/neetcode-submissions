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
        # If node has a previous node, link prev to next
        if node.prev:
            node.prev.next = node.next
        else:
            # node was head
            self.head = node.next

        # If node has a next node, link next to prev
        if node.next:
            node.next.prev = node.prev
        else:
            # node was tail
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

    def get(self, key: int) -> int:
        if key not in self.mapper:
            return -1

        node = self.mapper[key]

        # Accessing makes it most recently used
        self.remove(node)
        self.add_to_tail(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.mapper:
            node = self.mapper[key]
            node.value = value

            # Updating also makes it most recently used
            self.remove(node)
            self.add_to_tail(node)
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
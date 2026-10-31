class ListNode:
    def __init__(self,key: int, val: int = 0, next: Optional[ListNode] = None, prev: Optional[ListNode] = None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key





class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hasht = {}
        LEFT, RIGHT = ListNode(0), ListNode(0)
        LEFT.next = RIGHT
        RIGHT.prev = LEFT



    def get(self, key: int) -> int:
        if key in self.hasht:
            return self.hasht[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hasht:
            self.hasht[key].val = value
        else:
            if self.size == self.capacity:
                node = LEFT.next
                self.remove(node)
                del self.hast[node.key]

            
            else:
                newnode = ListNode(value)
                self.insertmru(newnode)
                self.hasht[key] = newnode
                

    
    def remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertmru(self, node: ListNode):
        RIGHT.prev.next = node
        node.prev = RIGHT.prev
        node.next = RIGHT
        RIGHT.prev = node


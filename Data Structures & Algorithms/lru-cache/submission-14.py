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
        self.LEFT, self.RIGHT = ListNode(0), ListNode(0)
        self.LEFT.next = self.RIGHT
        self.RIGHT.prev = self.LEFT



    def get(self, key: int) -> int:
        if key in self.hasht:
            return self.hasht[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hasht:
            self.hasht[key].val = value
        else:
            newnode = ListNode(key,value)
            if self.size == self.capacity:
                node = self.LEFT.next
                self.remove(node)
                del self.hasht[node.key]
                self.size -= 1
            
           
            self.insertmru(newnode)
            self.hasht[key] = newnode
            self.size += 1
                

    
    def remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertmru(self, node: ListNode):
        self.RIGHT.prev.next = node
        node.prev = self.RIGHT.prev
        node.next = self.RIGHT
        self.RIGHT.prev = node


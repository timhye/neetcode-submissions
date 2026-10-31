"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        store: Dict[Node,Node] = {}
        cur = head

        if cur is None:
            return None
        
        elif cur.next is None:
            start = Node(0)
            start.val = cur.val
            if cur.random == cur:
                start.random = start
            
            return start
        
        else:
            start = Node(0)
            while cur is not None:
                bn = Node(0)
                bn.val = cur.val
                store[cur] = bn
                cur = cur.next
                
            
            cur = head
            
            while cur is not None:
                if cur == head:
                    start.next = store[cur]
                
                if cur.next and cur.next in store:
                    store[cur].next = store[cur.next]
                
                if cur.random and cur.random in store:
                    store[cur].random = store[cur.random]
                
                cur = cur.next
            
            return start.next
                



            
                



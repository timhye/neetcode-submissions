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
        
        cur = head
        while cur is not None:
            new = Node(cur.val)
            new.next = cur.next
            cur.next = new
            cur = new.next
        
        #to attach the random pointers and assign them
        cur = head

        while cur is not None:
            if cur.random is None:
                cur.next.random = None
            cur.next.random = cur.random.next
            cur = cur.next.next
        
        #time to decouple
        cur = head
        next = cur.next
        newh = next
        while cur is not None:
            cur.next = next.next
            if cur.next:
                next.next = cur.next.next
            cur = cur.next
            next = next.next

        return newh
        # A->A'->B->B'->C->C'
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
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        #time to decouple
        cur = head
        while cur:
            newh = cur.next
            while cur is not None:
                copy = cur.next
                cur.next = copy.next
                if cur.next:
                    copy.next = cur.next.next
                cur = cur.next
                copy = copy.next

            return newh
        return
        # A->A'->B->B'->C->C'
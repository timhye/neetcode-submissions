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
        
        tmp = head
        rec = {}
        while tmp is not None:
            rec[tmp] = Node(tmp.val)
            tmp = tmp.next
    
        rec[None] = None
        
        # Now we have hashmap mapping original list node references to the new node references

        for old, new in rec.items():
            if old is not None and new is not None:  
                new.next = rec[old.next]
                new.random = rec[old.random]
        newhead = rec[head]

        return newhead


            
        
      
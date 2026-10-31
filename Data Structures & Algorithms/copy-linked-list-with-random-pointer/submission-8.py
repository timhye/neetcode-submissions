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
        rec = defaultdict(Node)
        while tmp is not None:
            rec[tmp] = Node(tmp.val)
            tmp = tmp.next
        
        # Now we have hashmap mapping original list node references to the new node references

        for old, new in rec.items():  
            new.next = rec[old.next]
            new.random = rec[old.random]
        newhead = rec[head]

        return newhead


            
        
      
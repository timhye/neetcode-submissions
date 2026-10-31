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
        store = defaultdict(set)
        cur = head
        start = Node()
        point = start
        cnt = 0

        if cur is None:
            return None
        
        elif cur.next is None:
            start.val = cur.val
            store[cur.val].add(cur)
            if cur.random == cur:
                start.random = cur
            
            return start

            
                



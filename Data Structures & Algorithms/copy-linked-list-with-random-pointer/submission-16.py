class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        tmp = head
        rec = {}

        # Pass 1: create every copied node
        while tmp is not None:
            rec[tmp] = Node(tmp.val)
            tmp = tmp.next

        rec[None] = None

        # Pass 2: connect next and random
        tmp = head
        while tmp is not None:
            new = rec[tmp]
            new.next = rec[tmp.next]
            new.random = rec[tmp.random]
            tmp = tmp.next

        return rec[head]
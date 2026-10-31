# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode()
        dummy.next = head
        count = 0

        cur, prev = dummy, None
        while cur is not None:
            if count == (left - 1):
                start = cur
            elif count >= left and count <= right:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            
            else:
                cur = cur.next
            count += 1

        
        start.next.next.next = next
        start.next = prev

        return dummy.next

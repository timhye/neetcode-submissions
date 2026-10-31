# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        length = 0
        check = head
        while check is not None:
            length += 1
            check = check.next
        idx = 0
        prev = None
        cur = head
        while idx != (length - n) and cur:
            prev = cur
            cur = cur.next
            idx += 1
        if prev:
            prev.next = cur.next
        else:
            head = cur.next
        
        return head
        
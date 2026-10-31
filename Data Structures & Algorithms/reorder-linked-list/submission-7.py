# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        prev = None

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        slow.next = None
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        tmp = head
        while tmp is not None and fast is not None:
            next = tmp.next
            tmp.next = fast
            fast = fast.next
            tmp.next.next = next
            tmp = next

        


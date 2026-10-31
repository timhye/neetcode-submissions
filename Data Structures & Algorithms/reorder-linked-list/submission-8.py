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
        last = None
        while last.next is not None:
            last = last.next
        while tmp is not None and last is not None:
            next = tmp.next
            tmp.next = last
            last = last.next
            tmp.next.next = next
            tmp = next

        


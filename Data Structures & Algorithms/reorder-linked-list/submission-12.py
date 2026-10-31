# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        #by here, the slow pointer is at 2 for [0,1,2,3,4,5] and [0,1,2,3,4]
        
        # to reverse the back end of the split list
        prev, cur = None, slow.next
       
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        slow.next = None

        start = head
        while prev is not None:
            ins = start.next
            start.next = prev
            next = prev.next
            prev.next = ins
            start = ins
            prev = next

        return
            
        
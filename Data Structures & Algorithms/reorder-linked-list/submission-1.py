# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        
        point = head.next
        prev = None
        while point is not None:
            next = point.next
            point.next = prev
            prev = point 
            point = next
        
        head.next = prev

        
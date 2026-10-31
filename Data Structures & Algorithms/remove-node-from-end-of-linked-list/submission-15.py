# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        length = 0
        tmp = dummy
        pt = dummy
        while tmp is not None:
            length += 1
            tmp = tmp.next
        
        length -= n
        if length < 0:
            pt.next = pt.next.next
        else:
            for i in range(length - 1):
                pt = pt.next
        
            pt.next = pt.next.next
        
        return dummy.next
        
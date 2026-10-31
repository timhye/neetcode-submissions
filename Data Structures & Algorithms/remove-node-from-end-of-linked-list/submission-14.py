# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        tmp = head
        while tmp is not None:
            length += 1
            tmp = tmp.next
        
        length -= (n + 1)
        tmp = head
        if length < 0:
            return None
        for i in range(length):
            tmp = tmp.next
        
        if tmp.next:
            tmp.next = tmp.next.next

        return head


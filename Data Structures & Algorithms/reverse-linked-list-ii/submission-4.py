# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        if not head or not head.next:
            return head
        cur = head
        front = None
        prev = None
    
        for i in range(1,left):
            front = cur
            cur = cur.next
        
        for i in range(right - left + 1):
            if i == 0:
                end = cur
            next = cur.next
            cur.next = prev 
            prev = cur
            cur = next

        if front: 
            front.next = prev     

            end.next = cur
            return head
        else:
            end.next = cur
            return prev    

            

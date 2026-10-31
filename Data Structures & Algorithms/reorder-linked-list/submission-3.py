# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        length = 0
        point = head
        while point is not None:
            length += 1
            point = point.next
        split = length // 2
        point2 = head
        prev2 = None
        for i in range(split):
            prev2 = point2
            point2 = point2.next
        
        prev2.next = None

        prev2 = None
        while point2 is not None:
            next2 = point2.next
            point2.next = prev2
            prev2 = point2
            point2 = next2
        point1 = head
        while point1 and prev2:
            next1 = point1.next
            point1.next = prev2
            next2 = prev2.next
            prev2.next = next1
            point1 = next1
            prev2 = next2
        
        point1.next = prev2
        
        
        
           
        

        

        
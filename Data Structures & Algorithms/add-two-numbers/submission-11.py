# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = l1, l2
        lh1, lh2 = 0,0
        carry = 0
        while h1 is not None:
            lh1 += 1
            h1 = h1.next
        
        while h2 is not None:
            lh2 += 1
            h2 = h2.next
        
        h1, h2 = l1, l2
        if lh1 >= lh2:
            c = h1
        else:
            c = h2

        prev = None
        while h1 is not None and h2 is not None:
            total = h1.val + h2.val
            if carry != 0:
                total += carry
                carry = 0
            if total > 9:
                carry = 1
                total = total % 10

            c.val = total
            h1 = h1.next
            h2 = h2.next
            prev = c
            c = c.next
        
        while c is not None:
            if carry != 0:
                check = c.val + carry
                if check > 9:
                    carry = 1
                    c.val = check % 10
                else:
                    c.val = check
                
            c = c.next
        
        if carry != 0:
            prev.next = ListNode(1)
        
        return l1 if lh1 >= lh2 else l2


       

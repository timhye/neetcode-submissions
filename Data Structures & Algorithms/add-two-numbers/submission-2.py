# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        num1 = 0
        mul1 = 1
        num2 = 0
        h3 = ListNode(0)
        prev = h3
        while h1 is not None:
            num1 += h1.val * mul1
            mul1 *= 10
            h1 = h1.next
        mul2 = 1
        while h2 is not None:
            num2 += h2.val * mul2
            mul2 *= 10
            h2 = h2.next
        
        num3 = num1 + num2
        if num3 == 0:
            return h3
        while num3 > 0:
            node = ListNode(num3 % 10)
            prev.next = node
            prev = node
            num3 //= 10

        return h3.next



        

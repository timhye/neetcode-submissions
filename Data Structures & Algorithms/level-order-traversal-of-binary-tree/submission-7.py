# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        process = deque([root])
        
        while len(process) > 0:
            lmt = len(process)
            arr = []
            while lmt > 0:
                check = process.pop()
                arr.append(check.val)
                lmt -= 1
                if check.left:
                    process.appendleft(check.left)
                if check.right:
                    process.appendleft(check.right)
            res.append(arr)
                
        return res
        

            
            
                    

        

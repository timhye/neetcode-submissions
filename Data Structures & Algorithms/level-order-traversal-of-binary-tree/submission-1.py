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
        process = deque([[root]])
        
        while process:
            arr = []
            ins = []
            check = process.pop()
            for node in check:
                if node.left:
                    arr.append(node.left)
                
                if node.right:
                    arr.append(node.right)
                
                ins.append(node)
                
            res.append(ins)
            
            process.appendleft(arr)
        
        return res
        

                    

        

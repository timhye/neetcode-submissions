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
        
        while len(process) > 0:
            arr = [] #for the list of nodes to be added to the queue to be processed
            ins = [] #for the nested list of values to be append to result arr
            check = process.pop() #will get [root] in the first iteration
            for node in check:
                if node.left:
                    arr.append(node.left)
                
                if node.right:
                    arr.append(node.right)
                
                ins.append(node.val)
                
            res.append(ins)
            
            if arr:
                process.appendleft(arr)
        
        return res
        

                    

        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque([root])
        res = []

        while queue:
            count = len(queue)
            while count > 0:
                process = queue.pop()
                if count == 1:
                    res.append(process.val)
                count -= 1

                if process.left:
                    queue.appendleft(process.left)
            
                if process.right:
                    queue.appendleft(process.right)
            

            
        
        
        return res
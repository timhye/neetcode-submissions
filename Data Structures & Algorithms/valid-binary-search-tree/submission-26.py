# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isvalid = True
        

        def dfs(node):
            nonlocal isvalid
            if node is None:
                return [float('inf'), float('-inf')]
            
            #What is returned shld be the min and max of subtree
            left = dfs(node.left)

            if not isvalid:
                return [float('inf'),float('-inf')]

            right = dfs(node.right)
            
            
            if left[1] < node.val < right[0]:
                return [min(left[0],node.val), max(right[1], node.val)]

            
            isvalid = False
            
            return [float('inf'), float('-inf')]
            
               

        
        dfs(root)
        

        return isvalid
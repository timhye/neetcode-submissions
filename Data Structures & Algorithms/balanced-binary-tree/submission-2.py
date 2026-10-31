# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#height needs to be propogated from children to parent, 
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isbal = True
        def dfs(node):
            nonlocal isbal
            if node is None:
                return 0
            
            lh = dfs(node.left)
            rh = dfs(node.right)

            if abs(lh - rh) > 1:
                isbal = False
            
            return max(lh, rh) + 1
        
        dfs(root)

        return isbal



               
        
        
        

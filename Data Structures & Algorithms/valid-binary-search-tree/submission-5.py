# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        seen = set()
        cur = True
        def dfs(node):
            if node is None:
                return True
            
            
            left = dfs(node.left)
            right = dfs(node.right)
            if not left or not right:
                return False
        

            if node.val in seen or (node.left and node.left.val >= node.val) or (node.right and node.right.val <= node.val):
                return False
            
            seen.add(node.val)
            

            
            return True
        
        return cur and dfs(root)

        

             


        

        
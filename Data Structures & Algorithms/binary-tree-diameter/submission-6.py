# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: 
        def dfs(node):
            height = 0
            if node is None:
                return 0
            
            elif node.left is None and node.right is None:
                return 1
            
            return max(dfs(node.left),dfs(node.right)) + 1

        lh = dfs(root.left)
        rh = dfs(root.right)

        return lh + rh + 1



        
        
        return max(self.diameterOfBinaryTree)

        
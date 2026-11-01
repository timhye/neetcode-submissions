# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        cur = True
        if root is None:
            return cur
        left = self.isValidBST(root.left)
        right = self.isValidBST(root.right)

        if (root.left and root.left.val > root.val) or (root.right and root.right.val < root.val):
            cur = False
        
        return left and cur and right 
        

        
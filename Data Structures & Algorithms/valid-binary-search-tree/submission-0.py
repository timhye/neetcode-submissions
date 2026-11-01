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
        left = isValidBST(node.left)
        right = isValidBST(node.right)

        if (root.left and root.left.val > node.val) or (node.right and node.right.val < node.val):
            cur = False
        
        return left and cur and right 
        

        
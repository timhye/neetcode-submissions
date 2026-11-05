# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isval = True

        def dfs(node):
            nonlocal isval
            
            if node is None:
                return [float('inf'), float('-inf')]
            
            left = dfs(node.left)

            if not isval:
                return [float('inf'), float('-inf')]

            right = dfs(node.right)
            

            if left[1] >= node.val or right[0] <= node.val:
                isval = False
                return [float('inf'), float('-inf')]

            return [min(left[0], node.val), max(node.val, right[1])]

        dfs(root)

        return isval


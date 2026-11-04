# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        if root is None:
            return count
        def dfs(node, val):
            nonlocal count
            if node is None:
                return
            
            if node.val >= val:
                count += 1
            
            upd = max(val, node.val)

            dfs(node.left, upd)
            dfs(node.right, upd)
        
        dfs(root, root.val)

        return count
            

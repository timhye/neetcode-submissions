# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, val):
            if node is None:
                return 0
            
            upd = max(val, node.val)
            gns = dfs(node.left, upd) + dfs(node.right, upd)
            if node.val >= val:
                gns += 1  

            return gns        
        
        

        return dfs(root, root.val)
            

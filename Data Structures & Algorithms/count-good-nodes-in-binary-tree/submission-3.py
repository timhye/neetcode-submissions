# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        cnt = 0
        
        def dfs(node, val):
            nonlocal cnt
            if node is None:
                return
            
            if node.val >= val:
                cnt += 1
            
            newv = max(val, node.val)

            dfs(node.left, newv)
            dfs(node.right, newv)
        
        dfs(root, root.val)

        return cnt 


        

        
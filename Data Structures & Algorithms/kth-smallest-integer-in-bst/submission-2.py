# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal? 
        order = 1
        ans = float('-inf')
        def dfs(node): #helps to calculate where it stands in the smallest 
            nonlocal order, ans
            if node is None:
                return
            
            
            dfs(node.left)
            if ans != float('-inf'):
                return
            if order == k:
                ans = node.val
                order += 1
                return
            else:
                order += 1

            dfs(node.right)
            
        
        dfs(root)
        return ans 

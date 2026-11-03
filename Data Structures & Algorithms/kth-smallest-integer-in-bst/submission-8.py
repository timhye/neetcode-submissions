# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        order = 1
        ans = float('-inf')
        def dfs(node, k):
            nonlocal order,ans
            if node is None:
                return 


            dfs(node.left, k)
            if order == -1:
                return 

            if order == k:
                ans = node.val
                order = -1
                return 
            else:
                order += 1

            dfs(node.right, k)
        
        dfs(root,k)
        
        return ans


        

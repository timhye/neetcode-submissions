# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k 
        found = 0
        val = 0
        def dfs(node):
            nonlocal count,found,val
            
            if node.left:
                dfs(node.left)

               
            
            if found:
                return 
         
            count -=1
            if count == 0:
                val = node.val
                found = 1
                return

            

            if node.right:
                dfs(node.right)

                    
            return 
        
        dfs(root)

        return val
            


        

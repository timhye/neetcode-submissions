# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isval = True
        seen = set()
        def dfs(node):
            nonlocal isval
            
            if node is None:
                return (0,0)
            
            
            leftlowest, lefthighest = dfs(node.left)
            rightlowest, righthighest = dfs(node.right)

            if lefthighest > node.val or rightlowest < node.val or node.val in seen or (node.left and node.left.val > node.val) or (node.right and node.right.val < node.val):
                return False

            seen.add(node.val)

            return leftlowest, righthighest


            


            
            

            
            return True
        
        return dfs(root)

        

             


        

        
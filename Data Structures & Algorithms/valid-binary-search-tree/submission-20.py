# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isvalid = True
        

        def dfs(node):
            nonlocal isvalid
            if node is None:
                return None
            
            #What is returned shld be the min and max of subtree
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                if left[1] < node.val < right[0]:          
                    return [left[0],right[1]]
                
                isvalid = False
                return None

            elif left:
                if left[1] < node.val:
                    return [left[0],node.val]
                isvalid = False
                return None
            elif right:
                if right[0] > node.val:
                    return [node.val,right[1]]
                isvalid = False
                return None 
            else:
                
                return [node.val,node.val]

        
        dfs(root)
        

        return isvalid
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(rootnode, subnode):
            if rootnode is None and subnode is None:
                return True
            
            elif (rootnode is None and subnode is not None) or (rootnode is not None and subnode is None):
                return False
            
            elif rootnode.val != subnode.val:
                return False

            left, right = dfs(rootnode.left, subnode.left),dfs(rootnode.right, subnode.right)
            
            
            return left and right
                
            
        if root is None:
            return False
        if root.val == subRoot.val and dfs(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
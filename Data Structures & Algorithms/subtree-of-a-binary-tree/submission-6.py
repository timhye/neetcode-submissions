# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        issub = False
        leftres = False
        rightres = False
        def dfs(node, arr):
            if node is None:
                arr.append(None)
                return
            
            left = dfs(node.left,arr)
            right = dfs(node.right,arr)
            arr.append(node.val)
                
        def check(rootnode, subnode):
            res1, res2 = [],[]

            dfs(rootnode, res1)
            dfs(subnode, res2)

            return res1 == res2
        if root is None:
            return False
        if root.val == subRoot.val:
            issub = check(root, subRoot)
        if issub:
            return issub
        else:
            if root.left:
                leftres = self.isSubtree(root.left, subRoot)
            
            if root.right:
                rightres = self.isSubtree(root.right, subRoot)
            
        return issub or leftres or rightres
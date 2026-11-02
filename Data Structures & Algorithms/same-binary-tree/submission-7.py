# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1, res2 = [], []

        def traverse(node, arr):
            if node is None:
                arr.append(None)
                return
            left = traverse(node.left, arr)
           
            right = traverse(node.right, arr)
            arr.append(node.val)
            return

        traverse(p, res1)
        traverse(q, res2)

        print(res1,res2)



        return res1 == res2

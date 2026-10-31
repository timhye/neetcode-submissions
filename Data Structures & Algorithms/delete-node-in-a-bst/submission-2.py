# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if root.left is None and root.right is None:
                return None
            
            elif root.left is None:
                return root.right


            elif root.right is None:
                return root.left
            
            else:
                check = root.right
                while check.left is not None:
                    check = check.left
                root.val = check.val
                root.right = self.deleteNode(root.right,check.val)
                return root

        return root

             


    

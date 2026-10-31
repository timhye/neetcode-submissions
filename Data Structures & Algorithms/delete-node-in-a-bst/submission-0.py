# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
    I think for now, from what I see, there are 2 types of nodes that can be deleted. One is a node with children, and one is a leaf node, right?

For the leaf node one, we just need to return something like none or something, so that when we return none, or we return minus 1 or something, we need to return some kind of sentinel value to show that the value can just be removed. When it gets returned to the preceding call that evoked it in the first place, it can essentially use that number to remove the relationship.

The other possibility is that we have a child, a node that we need to remove has children. For example, this is the simple case where, let's say, it has 1 and 4. In this case, we could either swap 1 with 3 or 4 with 3.

But then, we would also have to figure out the other case, which is what if it happens to be 3, and then 1 has more elements under it, and 4 does not. In this case, we would have to shift 4 to the top, or we could shift 2 to the top instead.

So let's say 3 to 1 to 2, and 3 to 4. And then we could either do the pre-order predecessor or in-order predecessor.

"""
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
                root = check.val
                root.right = self.deleteNode(root.right,check.val)
                return root

        return root

             


    

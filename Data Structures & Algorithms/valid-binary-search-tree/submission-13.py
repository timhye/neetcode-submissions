
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isval = True

        def dfs(node):
            nonlocal isval

            if node is None:
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            if not isval:
                return None

            # Validate the current node
            if left is not None and left[1] >= node.val:
                isval = False
                return None

            if right is not None and right[0] <= node.val:
                isval = False
                return None

            # Return the min and max of this entire subtree
            min_val = left[0] if left is not None else node.val
            max_val = right[1] if right is not None else node.val

            return (min_val, max_val)

        dfs(root)
        return isval

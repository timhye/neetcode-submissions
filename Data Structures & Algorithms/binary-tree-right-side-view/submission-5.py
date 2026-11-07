# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        queue = deque([root])
        while queue:
            cnt = len(queue)
            for i in range(cnt,0, - 1):
                node = queue.pop()
                if i == 1:
                    res.append(node.val)
                
                if node.left:
                    queue.appendleft(node.left)
                
                if node.right:
                    queue.appendleft(node.right)
        return res

            


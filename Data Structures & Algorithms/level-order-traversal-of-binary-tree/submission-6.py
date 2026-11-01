# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        store = defaultdict(list)
        res = []
        process = deque([[root,1]])
        
        while len(process) > 0:
            check = process.pop()
            store[check[1]].append(check[0].val)
            if check[0].left:
                process.appendleft([check[0].left, check[1] + 1])
            
            if check[0].right:
                process.appendleft([check[0].right, check[1] + 1])
        
        return list(store.values())
        

            
            
                    

        

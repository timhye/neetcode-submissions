class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        scratch = []
        res = []
        def dfs(i):
            if i == len(nums):
                res.append(list(scratch))
                return

            scratch.append(nums[i])
            dfs(i + 1)
            scratch.pop()
            dfs(i + 1)
        
        dfs(0)

        return res

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        scratch = []
        def dfs(i):
            if i == len(nums):
                res.append(list(scratch))
                return
            
            #choices are to put the cur val inside or not, so we do it first then reset and go down the other path 

            scratch.append(nums[i])
            dfs(i + 1)
            scratch.pop()
            dfs(i + 1)

        dfs(0)
        return res

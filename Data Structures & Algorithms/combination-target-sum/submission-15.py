class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        total = 0
        used = [False] * len(nums)
        scratch = []

        def dfs(total, i):
            if total > target or i > len(nums) - 1:
                return
            if total == target:
                res.append(list(scratch))
                return
            
            total += nums[i]
            scratch.append(nums[i])
            dfs(total, i)
            total -= nums[i]
            scratch.pop()
            dfs(total, i + 1)


            #for this the choices are to choose for the nums that are not used but maybe it shld be done sequentially. We can either choose to take the current number or take js carry on?
                     
            

        dfs(total,0)

        return res
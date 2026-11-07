class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        total, scratch = 0, []
        def dfs(i, totalval, scratchpad):
            if totalval > target:
                return
            elif totalval == target:
                res.append(list(scratchpad))
                return
            
            else:
                if i < len(nums):
                    totalval += nums[i]
                    scratchpad.append(nums[i])
                    dfs(i, totalval, scratchpad)
                    totalval -= nums[i]
                    scratchpad.pop()
                    dfs(i + 1, totalval, scratchpad)

                return
        
        dfs(0, total, scratch)

        return res

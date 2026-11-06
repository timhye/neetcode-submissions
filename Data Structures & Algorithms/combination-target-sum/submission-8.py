class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        total, scratch = 0, []
        res = []
        def dfs(i, totalval, scratcharr):
            if totalval > target:
                return
            elif totalval == target:
                    res.append(list(scratcharr))
                    return
                
            else:
                if i < len(nums):
                    totalval += nums[i]
                    scratcharr.append(nums[i])
                    dfs(i, totalval, scratcharr)
                    totalval -= nums[i]
                    scratcharr.pop()
                    dfs(i + 1, totalval, scratcharr)
                
                
                return
            
        dfs(0, total, scratch)

        return res 
            
            

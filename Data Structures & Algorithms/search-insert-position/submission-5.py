class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = len(nums)
        while l <= r:
            idx = (l + r) // 2
            if nums[idx] == target:
                return idx
            elif nums[idx] > target:
                res = idx
                r = idx - 1
            
            else:
                l = idx + 1

        return res
        
        


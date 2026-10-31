class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        idx = (l + r) // 2
        while l < r:
            idx = (l + r) // 2
            if nums[idx] == target:
                return idx
            elif nums[idx] > target:
                r = idx - 1
            
            else:
                l = idx + 1
        
        return idx


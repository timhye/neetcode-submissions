class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l < r:
            idx = (r - l + 1) // 2
            if nums[idx] == target:
                return idx
            elif nums[idx] < target:
                l = idx + 1     
            else:
                r = idx - 1
        
        return idx


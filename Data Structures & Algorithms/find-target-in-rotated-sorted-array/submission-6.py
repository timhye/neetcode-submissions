class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2

            if nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid
            else:
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
            
        
        return l


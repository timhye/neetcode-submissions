class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            
            elif nums[mid] == nums[left] == nums[right]:
                left += 1
                right -= 1
                
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                
                else:
                    left = mid + 1
            
            else:
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid
            
        return True if nums[left] == target else False
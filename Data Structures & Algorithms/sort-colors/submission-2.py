class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = mid = 0
        right = len(nums) - 1
        for i in range(len(nums)):
            if nums[mid] == 0:
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
                mid += 1
            
            elif nums[mid] == 1:
                mid += 1
                
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
        
        return nums
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nums[i] - 1] *= -1
            
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return nums[i]


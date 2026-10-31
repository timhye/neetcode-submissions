class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 99
                    
        for i in range(len(nums)):
            if nums[i] != 99:
                nums[abs(nums[i]) - 1] *= -1
        
        print(nums)
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return nums[i]


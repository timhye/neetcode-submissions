class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            if abs(nums[i]) < len(nums) and nums[i] != 0:
                if nums[abs(nums[i]) - 1] > 0:
                    nums[abs(nums[i]) - 1] *= -1
            
        
        for i in range(len(nums)):
            if i > 0:
                return i + 1
            
        if max(nums) == 0:
            return 1
        
        else: 
            return max(nums)
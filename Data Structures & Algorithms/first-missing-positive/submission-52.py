class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #iterate through array and preprocess array to deal with negatives and all, set to 0
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] > len(nums):
                nums[i] = len(nums) + 1
        
        #[0,0,0]
        for i in range(len(nums)):
            if nums[i] < len(nums) + 1 and nums[nums[i] - 1] > 0 and nums[i] > 0:
                nums[nums[i] - 1] *= -1
            
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
            
        return len(nums) + 1
                 
        



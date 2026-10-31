class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = 1
        val = nums[0]
        for i in range(1, len(nums)):
            if num == 0:
                val = nums[i]
                num += 1
                continue
                
            if nums[i] == val:
                num += 1
            
            else:
                num -= 1
        
        return val
            

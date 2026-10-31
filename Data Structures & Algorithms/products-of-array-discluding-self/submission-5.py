class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix, prefix = 1, 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
            res[len(nums) - 1 - i] *= postfix
            postfix *= nums[len(nums) - 1 - i]
        
        return res

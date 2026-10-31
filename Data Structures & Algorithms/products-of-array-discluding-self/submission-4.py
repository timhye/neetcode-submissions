class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1] * len(nums) ,[1] * len(nums)
        for i in range(1,len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        
        for j in range(len(nums) - 2,-1,-1 ):
            right[j] = right[j + 1] * nums[j + 1]     

        print(right)

        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = left[i] * right[i]

        return output   

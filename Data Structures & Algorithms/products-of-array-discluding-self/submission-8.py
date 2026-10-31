class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        point = 1
        for i in range(len(nums)):
            output[i] = point
            point *= nums[i]
        point = 1
        for j in range(len(nums) - 1, -1, - 1):
            output[j] *= point
            point *= nums[j]

        return output

            
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 2*10**31
            

        print(nums)

        for i in range(len(nums)):
            if abs(nums[i]) < len(nums) + 1:
                if nums[abs(nums[i]) - 1] > 0:
                    nums[abs(nums[i]) - 1] *= -1
        
        print(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        return len(num) + 1
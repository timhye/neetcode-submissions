class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = n + 1
        print(nums)
        for i in range(n):
            if abs(nums[i]) <= n and nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
        print(nums)
        for i in range(n):
            if nums[i] >= 0:
                return i + 1

        return n + 1 
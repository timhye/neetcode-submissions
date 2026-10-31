class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minL = float("inf")
        total = 0
        left = 0
        for right in range(len(nums)):
            total += nums[right]
            while total - nums[left] >= target:
                total -= nums[left]
                left += 1
            
            if total >= target:
                minL = min(minL, right - left + 1)

        return minL





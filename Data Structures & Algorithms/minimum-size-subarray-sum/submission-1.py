class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        minLen = 0
        length = 0
        left = 0
        total = 0

        for right in range(len(nums)):
            length += 1
            total += nums[right]

            if total < target:
                continue

            while total - nums[left] >= total:
                total -= nums[left]
                left += 1
                length -= 1
            
            minLen = min(minLen, length)

        return minLen
            


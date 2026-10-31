class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        minLen = float('inf')
        length = 0
        left = 0
        total = 0

        for right in range(len(nums)):
            length += 1
            total += nums[right]

            if total < target:
                continue

            while total - nums[left] >= target:
                total -= nums[left]
                left += 1
                length -= 1
            
            minLen = int(min(minLen, length))

        return minLen
            


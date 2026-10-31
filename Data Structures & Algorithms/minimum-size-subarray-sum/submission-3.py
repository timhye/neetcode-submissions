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

            print(total)
            while total - nums[left] >= target:
                total -= nums[left]
                left += 1
                length -= 1
            
            minLen = min(minLen, length)

        return minLen
            


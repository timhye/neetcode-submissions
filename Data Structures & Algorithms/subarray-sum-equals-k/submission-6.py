class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        total = 0
        num = 0
        right = 0
        while right < len(nums) and left <= right:
            total += nums[right]
            if total == k:
                num += 1
            elif total > k:
                while total > k:
                    left += 1
                    total -= nums[left]
                if total == k:
                    num += 1
            right += 1
        return num


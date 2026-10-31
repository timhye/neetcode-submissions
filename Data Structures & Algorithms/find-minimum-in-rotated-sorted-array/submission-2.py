class Solution:
    def findMin(self, nums: List[int]) -> int:
        small = nums[0]
        ref = nums[0]
        left, right = 1, len(nums)
        while left <= right:
            mid = left + (right - left) // 2
            idx = (len(nums) - mid) % len(nums)
            num = nums[idx]
            if num > ref:
                right = mid - 1
            else:
                small = num
                left = mid + 1
        
        return small

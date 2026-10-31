class Solution:
    def findMin(self, nums: List[int]) -> int:
        small = nums[0]
        ref = nums[0]
        left, right = 1, len(nums)
        while left <= right:
            mid = left + (right - left) // 2
            check = nums[::-1]
            check[:] = check[mid - 1::-1] + check[-1:mid - 2:-1]
            if check[0] > ref:
                right = mid - 1
            else:
                small = check[0]
                left = mid + 1
        
        return small

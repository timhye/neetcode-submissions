class Solution:
    def turn(self, nums, start, end):
        left, right = start, end
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        turn(nums, 0, len(nums) - 1)
        turn(nums, 0, k - 1)
        turn(nums, k, len(nums) - 1)
        
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
        self.turn(nums, 0, len(nums) - 1)
        self.turn(nums, 0, k - 1)
        self.turn(nums, k, len(nums) - 1)
        
class Solution:
    def turn(self, nums: List[int], left: int, right: int) -> None:
        l, r = left, right
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1



    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.turn(nums, 0, len(nums) - 1)
        self.turn(nums,0, k - 1)
        self.turn(nums, k, len(nums) - 1)

        
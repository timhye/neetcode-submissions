class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left, right):
            while left < right and right < len(nums):
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            print(nums)

        k = k % len(nums)
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k ,len(nums) - 1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if target in nums:
            check = len(nums) // 2
            if nums and nums[check] == target:
                return check
            elif nums[check] < target:
                print(nums[check+1:])
                return self.search(nums[check+1:],target)
            elif nums[check] > target:
                print(nums[:check-1])
                return self.search(nums[:check - 1],target)

        return -1



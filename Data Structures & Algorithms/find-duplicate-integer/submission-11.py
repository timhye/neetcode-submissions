class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while nums[fast] is not None and nums[nums[fast]] is not None:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if nums[slow] == nums[fast] and slow != fast:
                return nums[fast]
                
        return

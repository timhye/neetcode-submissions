class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while nums[fast] is not None and nums[nums[fast]] is not None:
            if nums[slow] == nums[fast]:
                break
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = nums[0]

        while nums[fast] is not None:
            if nums[fast] == nums[slow]:
                return nums[fast]
            fast = nums[fast]
            slow = nums[slow]
        
        return

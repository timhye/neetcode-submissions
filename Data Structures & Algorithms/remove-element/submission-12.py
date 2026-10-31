class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while nums[right] == val:
            right -= 1
        
        while left < right:
            if nums[left] == val:
                nums[left], nums[right] = nums[left] = nums[right]
                right -= 1
                left += 1
            
        return len(nums) - right

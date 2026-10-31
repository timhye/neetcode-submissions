class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        count = 0
        while nums[left] != val: left += 1
        while nums[right] != val: right -= 1
        while left < right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        for num in nums:
            if num == val: count += 1
        

        return count 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        border = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[border - 1]:
                nums[border] = nums[i]
                border += 1
            
        return border

        




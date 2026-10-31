class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[next - 1]:
                nums[next] = nums[i]
                next += 1
            
        return next

        




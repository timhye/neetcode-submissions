class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next = 1
        cnt = 1
        pivot = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != pivot:
                nums[next] = nums[i]
                pivot = nums[i]
                next += 1
                cnt += 1
            else:
                continue

        return cnt

        





class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        check = 1
        for num in nums:
            if num == check:
                check += 1
                continue
            
        return check
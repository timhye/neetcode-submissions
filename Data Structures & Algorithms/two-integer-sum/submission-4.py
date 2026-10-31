class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        data = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff not in data:
                data[n] = i
            else:
                return [n, data[diff]]

        
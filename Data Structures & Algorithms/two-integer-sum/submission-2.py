class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        data = {}

        for i,n in enumerate(nums):
            data[n] = i

        for i,n in enumerate(nums):
            diff = target - n
            if diff in data.keys() and data[diff] != i:
                return [i, data[diff]]   
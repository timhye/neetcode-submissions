class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        data = {}

        for k,num in enumerate(nums):
            diff = target - num
            if diff not in data:
                data[num] = k
            else:
                return [data[diff],k]


        
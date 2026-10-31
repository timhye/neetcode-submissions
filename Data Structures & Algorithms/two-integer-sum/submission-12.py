class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in store:
                return [store[val], i]
            
            else:
                store[nums[i]] = i

        return []
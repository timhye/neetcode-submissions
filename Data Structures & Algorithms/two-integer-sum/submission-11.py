class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for idx,num in enumerate(nums):
            check = target - num
            if check in store:
                
                return [min(idx, store[check]), max(idx, store[check])]
            else:
                store[num] = idx
        
        return 
        
        
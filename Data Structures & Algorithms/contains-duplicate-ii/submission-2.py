class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums.sort()
        i, j = 0, 0
        while i < len(nums)  and j < len(nums):
            if i != j:
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
                
                i += 1
            
            j += 1
        
        return False
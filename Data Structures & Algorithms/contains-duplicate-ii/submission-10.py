class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = defaultdict(list)
        left = 0
        for right in range(len(nums)):
            store[nums[right]].append(right)

            if len(store[nums[right]]) > 1 and abs(store[nums[right]][-1] - store[nums[right]][-2]) <= k:
                return True
            
            
    
        return False

        
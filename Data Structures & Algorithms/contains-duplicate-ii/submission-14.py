class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for right in range(len(nums)):
            if right > k:
                window.remove(right - k)
            
            if nums[right] in window:
                return True
            
            window.add(nums[right])
        
        return False
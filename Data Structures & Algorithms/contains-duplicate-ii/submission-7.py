class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record = {}
        for i in range(len(nums)):
            if nums[i] in record and i - record[nums[i]] <= k:
                return True
            
            record[nums[i]] = i

        return False


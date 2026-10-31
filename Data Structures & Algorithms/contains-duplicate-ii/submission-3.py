class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record = defaultdict(list)
        for i in range(len(nums)):
            record[nums[i]].append(i)
        
        for k,v in record.items():
            if len(v) > 1 and v[1] - v[0] <= k:
                return True
        
        return False

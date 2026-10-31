class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record = defaultdict(list)
        for i in range(len(nums)):
            record[nums[i]].append(i)
        print(record)

        for key,val in record.items():
            if len(val) > 1 and abs(val[1] - val[0]) <= k:
                return True
        
        return False

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps = {}
        prefixsum = 0
        count = 0
        for num in nums:
            ps[prefixsum] = ps.get(prefixsum,0) + 1
            prefixsum += num
            if ps.get(prefixsum - k, 0) == 0:
                continue
            count += ps[prefixsum - k]
        
        return count

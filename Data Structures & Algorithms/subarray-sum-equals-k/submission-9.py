class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps = {}
        prefix = 0
        count = 0
        for num in nums:
            ps[prefix] = ps.get(prefix,0) + 1
            prefix += num
            count += ps.get(prefix - k, 0)
        
        return count

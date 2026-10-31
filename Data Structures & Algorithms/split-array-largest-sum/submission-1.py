class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r
        def canSplit(largest):
            subarr = 0
            curSum = 0
            for num in nums:
                curSum += num
                if curSum >= largest:
                    subarr += 1
                    curSum = num
            return subarr + 1 <= k

        while l <= r:
            mid = l + (r - l) // 2
            if canSplit(mid):
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        
        return res

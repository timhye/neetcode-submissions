class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        store = defaultdict(int)
        store[0] = 1
        cnt = 0
        total = 0
        for right in range(len(nums)):
            total += nums[right]

            if (total - k) in store:
                cnt += store[total - k]

            store[total] += 1
        return cnt 


        
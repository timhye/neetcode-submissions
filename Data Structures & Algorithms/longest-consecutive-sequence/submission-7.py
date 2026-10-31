class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = defaultdict(int)
        lookup = {i:1 for i in nums}
        longest = 1
        for i in range(len(nums)):
            if lookup.get(nums[i] - 1, -5 * 10**9) == -5 *10**9:
                count = 1
                check = nums[i] + 1
                while lookup.get(check, -5 * 10**9) != -5 *10**9:
                    count += 1
                    check += 1
                longest = max(longest, count)

        return longest
                

                
                
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        rec = set(nums)
        longest = 0
        
        
        for key in rec:
            if key - 1 not in rec:
                keep = key
                count = 0
                while keep in rec:
                    count += 1
                    keep += 1

                longest = max(longest, count)

        return longest
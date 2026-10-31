class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        rec = {}
        longest = 0
        for num in nums:
            rec[num] = rec.get(num,0) + 1
        
        
        for key in rec:
            keep = key
            if key - 1 not in rec:
                count = 0
                while keep in rec:
                    count += 1
                    keep += 1

                longest = max(longest, count)

        return longest
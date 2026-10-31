class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        last_seen = { } #index which char was last seen
        left = 0 
        longest = 0

        for right, char in enumerate (s): 
            if char in last_seen: 
                left = max (left,last_seen [char] + 1 ) #move window

            last_seen [char] = right
            longest = max (longest, right - left + 1)

        return longest   


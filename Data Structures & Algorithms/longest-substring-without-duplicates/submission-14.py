class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left, right = 0,0
        rec = {}
        while right < len(s):
            
            rec[s[right]] = rec.get(s[right],0) + 1
            #dvdf
        
            while rec[s[right]] > 1:
                rec[s[left]] = rec.get(s[left]) - 1
                left += 1
            
            longest = max(longest, right - left + 1)
            
            right += 1
        
        return longest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        longest = 0
        left, right = 0, 0
        rec = {}
        while left < len(s) and right < len(s):
            if s[right] not in rec:
                rec[s[right]] = 1
                right += 1
            else:
                while left < right and rec.get(s[right]) >= 1:
            
                    rec[s[right]] = rec.get(s[right]) - 1
                    
                    left += 1
                            
            
            longest = max(longest, right - left)
        
        return longest





        return longest


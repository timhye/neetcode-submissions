class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxl = 0
        store = {}
        for right in range(len(s)):
            store[s[right]] += 1
            while max(store.values()) > 1:
                store[s[l]] -= 1
                l += 1
            
            maxl = max(maxl, right - l + 1)
        
        return maxl
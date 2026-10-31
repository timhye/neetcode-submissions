class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl = 0
        store = defaultdict(int)
        left = 0
        for right in range(len(s)):
            store[s[right]] += 1
            
            while store[s[right]] > 1:
                store[s[left]] -= 1
                left += 1
            
            maxl = max(maxl, right - left + 1)

        return maxl
            


           


            

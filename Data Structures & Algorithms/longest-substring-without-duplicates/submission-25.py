class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = defaultdict(int)
        left, right = 0, 0
        maxL = 0
        while right < len(s):
            store[s[right]] += 1
            while store[s[right]] > 1:
                store[s[left]] -= 1
                left += 1

            length = right - left + 1
                
            maxL = max(maxL, length)
            right += 1
            
        return maxL
                
            
            


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        store = defaultdict(int)
        maxL= 0
        maxf = 0
        for right in range(len(s)):
            store[s[right]] += 1
            
            while ((right - l + 1) - maxf) > k:
                store[s[l]] -= 1
                l += 1
            
            maxL = max(maxL, right - l + 1)
            maxf = max(maxf, store[s[right]])
        
        return maxL


 
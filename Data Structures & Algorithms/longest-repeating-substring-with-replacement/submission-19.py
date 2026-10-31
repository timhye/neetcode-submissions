class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        store = defaultdict(int)
        maxL= 0
        cha = s[0]
        for right in range(len(s)):
            store[s[right]] += 1
            if store[s[right]] >= store[cha]:
                cha = s[right]

            while ((right - l + 1) - store[cha]) > k:
                store[s[l]] -= 1
                l += 1
            
            
            maxL = max(maxL, right - l + 1)
        
        return maxL


 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxf = 0
        maxl = 0
        store = defaultdict(int)

        for right in range(len(s)):
            store[s[right]] += 1
            maxf = max(maxf, store[s[right]])
            while (right - left + 1) - maxf > k:
                store[s[left]] -= 1
                left += 1
            
            maxl = max(maxl, right - left + 1)
        
        return maxl

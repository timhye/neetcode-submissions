class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxL = 0
        left = 0
        maxFreq = 0
        store = defaultdict(int)
        for right in range(len(s)):
            store[s[right]] += 1
            maxFreq = max(maxFreq, store[s[right]])
            
            while (right - left + 1) - maxFreq> k:
                store[s[left]] -= 1
                left += 1
                
            maxL = max(maxL, right - left + 1)

        return maxL
        
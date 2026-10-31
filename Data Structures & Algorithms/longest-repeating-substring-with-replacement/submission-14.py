class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxL = 0
        left = 0
        store = defaultdict(int)
        for right in range(len(s)):
            store[s[right]] += 1
            
            while (right - left + 1) - max(store.values())> k:
                store[s[left]] -= 1
                left += 1
                
            maxL = max(maxL, right - left + 1)

        return maxL
        
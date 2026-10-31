class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxl = 0
        left = 0
        maxfreq = 0
        store = defaultdict(int)
        for right in range(len(s)):
            store[s[right]] += 1
            if store[s[right]] > maxfreq:
                maxfreq = store[s[right]]

            while (right - left + 1) - maxfreq > k:
                left += 1
                store[s[left]] -= 1
            
            maxl = max(maxl, right - left + 1)

        return maxl


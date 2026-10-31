class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxlen = 0
        maxfreq = 0
        store = defaultdict(int)
        
        for right in range(len(s)):
            store[s[right]] += 1
            maxfreq = max(maxfreq, store[s[right]])

            while (right - left + 1) - maxfreq > k:
                store[s[left]] -= 1
                left += 1
            

            maxlen = max(maxlen, right - left + 1)
        
        return maxlen

            

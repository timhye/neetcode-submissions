class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        rec = defaultdict(int)
        maxlength = 0
        maxfreq = 0
        for right in range(len(s)):
            rec[s[right]] += 1     
            maxfreq = max(maxfreq, rec[s[right]])       
            if (right - left + 1) - maxfreq > k:
                rec[s[left]] -= 1
                left += 1
            
            maxlength = max(maxlength, right - left + 1)

        
        return maxlength

             
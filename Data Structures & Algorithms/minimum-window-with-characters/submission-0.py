class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r = 0, len(s) - 1
        check = Counter(t)
        minLen = len(s)
        for right in range(len(s)):
            if s[right] in check:
                check[s[right]] -= 1
            
        if any(value >= 1 for value in check.values()):
            return ""
        
        while l < len(s):
            if s[l] in check:
                check[s[l]] += 1
            l += 1
            if all(value <= 0 for value in check.values()):
                minLen = min(minLen, r - l + 1)
            else:
                break
            
        return minLen
            
        
        
        

        

            


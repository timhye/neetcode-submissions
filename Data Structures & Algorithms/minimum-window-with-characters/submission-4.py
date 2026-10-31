class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        check = Counter(t)
        bestleft = 0
        minLen = float("inf")
        for right in range(len(s)):
            if s[right] in check:
                check[s[right]] -= 1
            while all(value <= 0 for value in check.values()):
                newLen = right - l + 1
                if newLen < minLen:
                    bestleft = l
                    minLen = newLen
                
                if s[l] in check:
                    check[s[l]] += 1
                l += 1
        return s[bestleft:bestleft + minLen] if minLen != float("inf") else ""
                    

            
        
        
        
        

        

            


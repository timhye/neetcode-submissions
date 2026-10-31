class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        check = Counter(t)
        bestleft = 0
        minLen = len(s)
        for right in range(len(s)):
            if s[right] in check:
                check[s[right]] -= 1
            if all(value <= 0 for value in check.values()):
                while right - l + 1 >= len(t):
                    newLen = right - l + 1
                    if newLen < minLen:
                        bestleft = l
                        minLen = newLen
                    if s[l] in check:
                        check[s[l]] += 1
                    l += 1
        return s[bestleft:bestleft + minLen]
                    

            
        
        
        
        

        

            


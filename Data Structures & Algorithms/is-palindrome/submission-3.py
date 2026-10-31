class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start = 0
        end = len(s) - 1

        while start < end:
            while not s[start].isalnum() and start < end:
                start += 1
                pass
                
            while not s[end].isalnum() and end > start:
                end -= 1
                pass
            if s[start] != s[end]:
                print(s[start], s[end])
                return False
            start += 1
            end -= 1
        
        return True
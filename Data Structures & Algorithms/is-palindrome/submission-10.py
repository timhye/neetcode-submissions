class Solution:
    def isPalindrome(self, s: str) -> bool:

        nc = ""
        for c in s:
            if c.isalnum():
                nc += c.lower()


        return nc == nc[::-1]
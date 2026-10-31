class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [char.lower() for char in s if char.isalnum()]

        left, right = 0, len(s_list) - 1
        while left < right:
            if left != right:
                return False

        return True
        
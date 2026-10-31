class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = [char for char in s if char.isalnum()]
        l, r = 0, len(arr)
        while l < r:
            if arr[l].lower() == arr[r].lower():
                l += 1
                r -= 1
        
            else:
                return False
        
        return True


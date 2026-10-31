class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        mid = x // 2
        ans = 0
        while left <= right:
            
            if mid * mid < x:
                ans = mid
                left = mid + 1
                
            else:
                right = mid - 1
            
            mid = left + (right - left) // 2
        
            
        return ans
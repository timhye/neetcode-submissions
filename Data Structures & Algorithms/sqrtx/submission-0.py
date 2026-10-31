class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        mid = x // 2
        while left <= right:
            if mid * mid == x:
                return mid
            
            elif mid * mid < x:
                left = mid + 1
                
            else:
                right = mid - 1
            
            mid = left + (left + right) // 2
        
            
         
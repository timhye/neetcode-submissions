class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0 , len(height) - 1
        amt = 0
        left, right = height[l], height[r] 
        while l < r:
            if left <= right:
                amt += (min(left,right) - height[l])
                l += 1
                left = max(left, height[l])

            else:
                amt += (min(left,right) - height[r]) 
                r -= 1
                right = max(right, height[r])
        
        return amt
            

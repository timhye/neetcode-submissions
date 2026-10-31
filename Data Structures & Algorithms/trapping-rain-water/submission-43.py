class Solution:
    def trap(self, height: List[int]) -> int:
        amt = 0
        l, r  = 0, len(height) - 1
        leftmax = height[0]
        rightmax = height[-1]
        while l < r:
            if leftmax <= rightmax:
                amt += leftmax - height[l]
                l += 1
                leftmax = max(leftmax, height[l])
            else:
                amt += rightmax - height[r]
                r -= 1
                rightmax = max(rightmax, height[r])
        
        return amt
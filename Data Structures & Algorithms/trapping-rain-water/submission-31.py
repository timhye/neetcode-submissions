class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftmax, rightmax = height[0], height[-1]
        amt = 0
        while left < right:
            if leftmax < rightmax:
                amt += leftmax - height[left]
                left += 1
                leftmax = max(leftmax, height[left])
            
            else:
                amt += rightmax - height[right]
                right -= 1
                rightmax = max(rightmax, height[right])

        return amt



        

        
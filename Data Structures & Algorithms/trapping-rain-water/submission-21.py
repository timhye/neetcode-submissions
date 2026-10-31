class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = height[0]
        left, right = 0, len(height) - 1
        rightmax = height[len(height) - 1]
        water = 0
        while left < right:
            if leftmax < rightmax:
                water += leftmax - height[left]
                left += 1
                leftmax = max(leftmax, height[left])
            
            else:
                water += rightmax - height[right]
                right -= 1
                rightmax = max(rightmax, height[right])

        return water
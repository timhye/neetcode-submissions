class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = height[0]
        left, right = 0, 0
        rightmax = height[len(height) - 1]
        water = 0
        while left < right:
            if leftmax < rightmax:
                water += max(0,leftmax - height[left])
                left += 1
                leftmax = max(leftmax, height[left])
            
            else:
                water += max(0, rightmax - height[right])
                right -= 1
                rightmax = max(rightmax, height[right])

        return water
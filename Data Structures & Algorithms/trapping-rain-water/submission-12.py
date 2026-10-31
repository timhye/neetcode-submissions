class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = height[0]
        left = 0
        rightmax = height[len(height) - 1]
        right = len(height) - 1
        water = 0
        for i in range(len(height)):
            if leftmax < rightmax:
                water += max(0,leftmax - height[left])
                left += 1
                leftmax = max(leftmax, height[left])
            
            else:
                water += max(0, rightmax - height[right])
                right -= 1
                rightmax = max(rightmax, height[right])

        return water
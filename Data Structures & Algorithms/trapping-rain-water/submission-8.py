class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = [0] * len(height)
        left = height[0]
        for i in range(len(height)):
            leftmax[i] = left
            left = max(left, height[i])
        
        print(leftmax)
        rightmax = [0] * len(height)
        right = height[len(height) - 1]
        for i in range(len(height) - 1, -1, -1):
            rightmax[i] = right
            right = max(right, height[i])
        print(rightmax)

        water = 0
        for i in range(len(height)):
            water += max(0, min(leftmax[i], rightmax[i])- height[i])
        return water


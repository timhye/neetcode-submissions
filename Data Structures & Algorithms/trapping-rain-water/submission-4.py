class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = height[0]
        right_max = height[len(height) - 1]
        water = 0
        for i in range(len(height)):
            if left_max < right_max:
                left_max = max(left_max, height[i])
                water += left_max - height[i]
            else:
                right_max = max(right_max, height[i])
                water += right_max - height[i]

        
        return water


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = height[0]
        right_max = height[len(height) - 1]
        left, right = 0, len(height) - 1
        water = 0
        for i in range(len(height)):
            if left_max < right_max:               
                water += (left_max - height[left])
                left += 1
                left_max = max(left_max, height[left])
                
            else:
                water += (right_max - height[right])
                right -= 1
                right_max = max(right_max, height[right])
                

        
        return water


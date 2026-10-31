class Solution:
    def trap(self, height: List[int]) -> int:
        """formula for the amount of water at each index is 
        min(left[i], right[i]) - height[i]"""
        amt = 0
        left = height[0] * len(height)
        right = height[-1] * len(height)
        for i in range(1,len(height)):
            left[i] = max(left[(i-1)],height[i])

        for i in range(len(height)-2,-1,-1):
            right[i] = max(right[i + 1],height[i])

        for i in range(len(height)):
            amt += (min(left[i], right[i]) - height[i])
        
        return amt


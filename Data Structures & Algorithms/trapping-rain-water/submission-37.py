class Solution:
    def trap(self, height: List[int]) -> int:
        amt = 0
        left = [0] * len(height)
        right = [0] * len(height)
        for i in range(1,len(height)):
            if height[i] > left[i - 1]:
                left[i] = height[i]
            else:
                left[i] = left[i - 1]
        
        for i in range(len(height) - 2, -1, -1):
            if height[i] > right[i + 1]:
                right[i] = height[i]
            else:
                right[i] = right[i + 1]

        for i in range(len(height)):
            amt += (min(left[i], right[i]) - height[i])
        


        return amt
class Solution:
    def trap(self, height: List[int]) -> int:
        amt = 0
        left = [0] * len(height)
        for i in range(1,len(height)):
            if height[i] > height[i - 1]:
                left[i] = height[i]
            else:
                left[i] = height[i - 1]
        
        print(left)

        return
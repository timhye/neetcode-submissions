class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxA = max(area, maxA)

            if nums[l] >= nums[r]:
                r -= 1
            else:
                l += 1
        
        return maxA
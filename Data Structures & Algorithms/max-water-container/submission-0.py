class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxA = -1
        while left < right:
            area = (right - left) * min(heights[left], heights[right])

            maxA = max(maxA, area)

            if min(heights[left], heights[right]) == heights[left]:
                left += 1
            else:
                right -= 1

        return maxA
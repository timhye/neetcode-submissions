from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        dq = deque()

        for i in range(len(nums)):
            # Remove indices that are outside the window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller values from the right
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            # Add the current index
            dq.append(i)

            # Record the maximum after forming a full window
            if i >= k - 1:
                output.append(nums[dq[0]])

        return output
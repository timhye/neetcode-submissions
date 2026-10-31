class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2

            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours <= h:
                # mid works, but perhaps a smaller speed also works
                right = mid
            else:
                # mid is too slow, so all speeds <= mid are too slow
                left = mid + 1

        return left
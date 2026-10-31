class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        can = -1
        req = k
        while left <= right:
            mid = left + (right - left + 1) // 2
            if arr[mid] == x:
                break
            elif arr[mid] < x:
                can = mid
                left = mid + 1
            else:
                right = mid - 1
        l, r = can, can
        while l > 0 and r < len(arr) - 1 and req > 0:
            l -= 1
            r += 1 
            if abs(arr[can] - arr[l]) <= abs(arr[r] - arr[can]):
                r -= 1
            else:
                l += 1
            req -= 1
        if l <= 0:
            while r < len(arr) - 1 and req > 0:
                r += 1
                req -= 1
        if r >= len(arr) - 1:
            while l >= 0 and req > 0:
                l -= 1
                req -= 1
        
        return arr[l:r]

        


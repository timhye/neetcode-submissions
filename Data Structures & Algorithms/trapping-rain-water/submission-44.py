class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0 , len(height) - 1
        amt = 0
        left, right = nums[l], nums[r] 
        while l < r:
            if left <= right:
                amt += (min(left,right) - nums[l])
                l += 1
                left = max(left, nums[l])

            else:
                amt += (min(left,right) - nums[r]) 
                r -= 1
                right = max(right, nums[r])
        
        return amt
            

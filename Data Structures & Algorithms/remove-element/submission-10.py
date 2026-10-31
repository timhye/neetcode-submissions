class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt,l,r = 0,0, len(nums) - 1
        
        while l < r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            
            else:
                l += 1
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                cnt += 1
            else:
                break
    
        return len(nums) - cnt
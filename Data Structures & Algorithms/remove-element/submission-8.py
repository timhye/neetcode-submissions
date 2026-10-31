class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt,l,r = 0,0, len(nums) - 1
        if not nums:
            return 0
        
        if len(nums) == 1 and nums[0] == val:
            return 0
            
        while l < r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                cnt += 1
            
            else:
                l += 1
        print(nums)
        return (len(nums) - cnt)
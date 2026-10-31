class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a,b,c = 0,0, len(nums) - 1
        while b <= c:
            if nums[b] == 2:
                nums[c], nums[b] = nums[b], nums[c]
                c -= 1
            
            elif nums[b] == 1:
                b += 1
            
            else:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b += 1
        
        return nums
        
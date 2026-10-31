class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        pivot = 0
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            pivot = i
            left = pivot + 1
            right = len(nums) - 1
            while left < right:
                if  0 < nums[left] + nums[right] + nums[pivot]:
                    right -= 1
                elif  0 > nums[left] + nums[right] + nums[pivot]:
                    left += 1
                
                else:
                    ans.append([nums[pivot], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                
        return ans

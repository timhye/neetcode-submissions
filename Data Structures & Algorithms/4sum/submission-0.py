class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        seen = []
        if len(nums) < 4:
            return [nums]
        for i in range(len(nums)-3):
            if i < len(nums) - 3 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1,len(nums)-2):
                if j > i + 1 and nums[j] == nums[j -1]:
                    continue
                target -= (nums[i] + nums[j])
                l = j + 1
                r = len(nums) -1
                while l < r:
                    total = nums[l] + nums[r]
                    if total == target:
                        seen.append([nums[i],nums[j],nums[l],nums[r]])
                        i += 1
                        r -= 1
                        while nums[i] == nums[i - 1]:
                            i += 1
                        while nums[r] == nums[r + 1]:
                            r -= 1
                    if total < target:
                        l += 1
                    if total > target:
                        r -= 1 


            
            
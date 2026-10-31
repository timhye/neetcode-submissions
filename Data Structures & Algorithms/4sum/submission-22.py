class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                a, b = j + 1, len(nums) - 1
                while a < b:
                    total = nums[i] + nums[j] + nums[a] + nums[b]
                    if total < target:
                        a += 1
                    
                    elif total > target:
                        b -= 1
                    
                    else:
                        res.append([nums[i],nums[j], nums[a], nums[b]])
                        a += 1
                        b -= 1
                        while a < b and nums[a] == nums[a - 1]:
                            a += 1
                        while a < b and nums[b] == nums[b + 1]:
                            b -= 1

        return res
                        

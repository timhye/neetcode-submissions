class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                f, s = j + 1, len(nums) - 1
                while f < s:
                    total = nums[i] + nums[j] + nums[f] + nums[s]
                    if total < target:
                        f += 1
                    elif total > target:
                        s -= 1
                    else:
                        res.append([nums[i], nums[j], nums[f], nums[s]])
                        f += 1
                        s -= 1
                        while f < s and nums[f] == nums[f - 1]:
                            f += 1
                        while f < s and nums[s] == nums[s + 1]:
                            s -= 1
        return res
                
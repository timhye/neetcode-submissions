class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = {}
        major[nums[0]] = 1
        num = nums[0]
        for i in range(1,len(nums)):
            if major.get(num, 0) == 0:
                major[nums[i]] = 1
                num = nums[i]
            if nums[i] in major:
                major[nums[i]] += 1
            
            else:
                major[num] -= 1

        return num

                
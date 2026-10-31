class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first, second = 0, 0
        cnt = 0
        while second < len(nums):
            if first != second:
                if nums[first] == nums[second]:
                    del nums[second]

                else:
                    first = second

            second += 1
            cnt += 1
        print(cnt)
        return cnt


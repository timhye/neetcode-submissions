class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = Counter(nums)
        return check.most_common(1)[0]
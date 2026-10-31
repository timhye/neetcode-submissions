class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        record = defaultdict(list)
        i = 0
        for num in nums:
            record[num].append(i)
            i += 1
        
        nums[:] = [0] * len(record[0]) + [1] * len(record[1]) + [2] * len(record[2])
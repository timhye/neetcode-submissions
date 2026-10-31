class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # idea is max only 2 elements can appear more than floor(n/3) times
        record = defaultdict(int)
        res = []
        for num in nums:
            record[num] += 1
        
        for num,freq in record.items():
            if freq > len(nums) // 3:
                res.append(num)

        return res



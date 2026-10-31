class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        record1 = defaultdict(int)
        res = []
        for num in nums:
            record1[num] += 1

            if len(record1) <= 2:
                continue
            record2 = defaultdict(int)
            for n,c in record1.items():
                if c > 1:
                    record2[n] = c - 1
            
            record1 = record2

        for num in record1:
            if nums.count(num) > len(nums)//3:
                res.append(num)
        return res
                    
                
                
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        record = defaultdict(int)
        for num in nums:
            record[num] += 1
            if len(record) > 2:
                for k,v in record.items():
                    record[k] -= 1
                
                record = {k:v for k,v in record.items() if v != 0}
        
        res = []
        for k,v in record.items():
            if v > len(nums)//3:
                res.append(k)
        return res
                
                
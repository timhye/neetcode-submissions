class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #dedup, arrange, check for > by 1 for each progressive entry, then increment length until condition doesnt hold
        record = {}

        if len(nums) <= 0:
            return 0
        for num in nums:
            record[num] = record.get(num,0) + 1
        
        maxlen = -1

        for num in record:
            checker = num - 1
            if checker not in record:
                length = 1
                check = num + 1
                while check in record:
                    length += 1
                    check += 1
                
                maxlen = max(maxlen, length)

        return maxlen
            




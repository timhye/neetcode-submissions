class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #dedup, arrange, check for > by 1 for each progressive entry, then increment length until condition doesnt hold
        record = {}
        maxseq = 0
        for num in nums:
            record[num] = record.get(num, 0) + 1
        
        for key in record:
            if (key - 1) not in record:
                count = 1
                next = key + 1
                while next in record:
                    count += 1
                    next += 1
            
                maxseq = max(maxseq, count)
        
        return maxseq



       


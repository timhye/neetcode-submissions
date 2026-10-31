class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = {}
        for i in nums:
            record[i] = record.get(i,0) + 1
        
        freq = {i:[] for i in range(1,len(nums))}
        print(freq)
        for num,feq in record.items():
            freq[feq].append(num)
        print(freq)
        
        topk = []

        for i in range(len(nums) - 1, -1,-1):
            if not freq[i]:
                continue
            else:
                for num in freq[i]:
                    if len(topk) == k:
                        return topk
                    topk.append(num)
        
        return topk
            


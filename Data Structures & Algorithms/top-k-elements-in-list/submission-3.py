class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = {}
        for i in num:
            record[i] = record.get(i,0) + 1
        
        freq = defaultdict(list)
        for num,feq in record.items():
            freq[feq].append(num)
        
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
            


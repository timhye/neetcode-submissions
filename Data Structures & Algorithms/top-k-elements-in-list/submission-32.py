class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        store = defaultdict(int)
        rec = defaultdict(list)
        for num in nums:
            store[num] += 1
        
        for i,v in store.items():
            rec[v].append(i)
        
        for i in range(len(nums) - 1,-1,-1):
            while len(rec[i]) > 0 and len(res) != k:
                res.append(rec[i].pop())
        
        return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = Counter(nums)
        for i in x.keys():
            if len(res) == k:
                return res
            res.append(i)
        
        return res

            


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = Counter(nums)
        print(freq)
        
        return list(freq.keys)[:k]

            


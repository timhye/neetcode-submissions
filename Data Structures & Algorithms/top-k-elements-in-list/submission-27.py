class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = Counter(nums)
        for num,fq in freq.most_common():
            if len(res) == k:
                return res
            res.append(num)

        return res

            


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        for num in nums:
            freq[num] = freq.get(num,0) + 1

        for k,v in freq.items():
            if v > len(nums) // 3:
                res.append(k)

        return k
        
        
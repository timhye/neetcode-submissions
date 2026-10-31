class Solution:
    def merge(self, ara: List[int], arb: List[int]):
        a, b = 0,0
        res = []
        while a < len(ara) and b < len(arb):
            if ara[a] <= arb[b]:
                res.append(ara[a])
                a += 1
            else:
                res.append(arb[b])
                b += 1
        
        res.extend(ara[a:])
        res.extend(arb[b:])

        return res
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left,right)        
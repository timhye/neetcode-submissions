class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)
        for num in nums:
            store[num] += 1
        freq = defaultdict(list)
        for val, feq in store.items():
            freq[feq].append(val)
        ans = []
        check = k
        for i in range(len(nums),-1,-1):
            while freq[i] and check > 0:
                ans.append(freq[i].pop())
        
        return ans

        
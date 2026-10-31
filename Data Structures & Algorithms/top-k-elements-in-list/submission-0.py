class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = {}
        base = nums[0]
        first, second = 0,0
        count = 0
        for i in range(len(nums)):
            if nums[second] == first:
                if record.get(first,0) == 0:
                    record[first] = 1
                else:
                    record[first] += 1
                second += 1
            
            else:
                first = second
        
        freq = [[] for _ in range(len(nums) + 1)]
        for k,v in record.items():
            if k not in freq[v]:
                freq[v].append(k)
        
        result = []
        track = len(nums)

        for i in range(len(nums)):
            for num in freq[track]:
                if num not in result and len(result) != 3:
                    result.append(num)
            
            track -= 1

        return result

            



        
            


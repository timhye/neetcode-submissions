class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = {}
        for num in nums:
            record[num] = record.get(num,0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for key,value in record.items():
            freq[value].append(key)
        
        result = []
        track = len(nums)

        for i in range(len(nums)):
            for num in freq[track]:
                if num not in result and len(result) != k:
                    result.append(num)
            
            track -= 1

        return result

            



        
            


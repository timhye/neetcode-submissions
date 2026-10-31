class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(l1: List[int], l2: List[int]):
            i, j = 0,0
            res = []
            while i < len(l1) and j < len(l2):
                if l1[i] >= l2[j]:
                    res.append(l1[i])
                    i += 1
                else:
                    res.append(l2[j])
                    j += 1
            
            if i >= len(l1):
                while j < len(l2):
                    res.append(l2[j])
                    j += 1
            
            else:
                while i < len(l1):
                    res.append(l1[i])
                    i += 1
            
            return res

        def split(arr: List[int]):
            if len(arr) == 1:
                return arr
            
            else:
                mid = len(arr) // 2
                return merge(split(arr[:mid]) + split(arr[mid:]))    


        return split(nums)
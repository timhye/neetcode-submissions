class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1: List[int], arr2: List[int]):
            res = []
            a, b = 0, 0
            while a < len(arr1) and b < len(arr2):
                if arr1[a] <= arr2[b]:
                    res.append(arr1[a])
                    a += 1
                else:
                    res.append(arr2[b])
                    b += 1
            
            if a >= len(arr1):
                while b < len(arr2):
                    res.append(arr2[b])
                    b += 1
            
            else:
                while a < len(arr1):
                    res.append(arr1[a])
                    a += 1
            
            return res


        if len(nums) == 1 or len(nums) == 0:
            return nums

                


        
        mid = len(nums) // 2
        return merge(self.sortArray(nums[:mid]), self.sortArray(nums[mid:]))

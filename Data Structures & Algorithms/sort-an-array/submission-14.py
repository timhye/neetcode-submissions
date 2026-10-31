class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2):
            a1, a2, r1 = 0, 0, 0

            res = [0] * (len(arr1) + len(arr2))
            while a1 < len(arr1) and a2 < len(arr2):
                if arr1[a1] <= arr2[a2]:
                    res[r1] = arr1[a1]
                    a1 += 1
                else:
                    res[r1] = arr2[a2]
                    a2 += 1
                
                r1 += 1
            
            if a1 == len(arr1):
                while a2 < len(arr2):
                    res[r1] = arr2[a2]
                    a2 += 1
                    r1 += 1
            
            else:
                while a1 < len(arr1):
                    res[r1] = arr1[a1]
                    a1 += 1
                    r1 += 1
            
            return res

        def spliter(arr):
            if len(arr) <= 1:
                return arr
            else:
                mid = len(arr)//2
                return merge(spliter(arr[:mid]),spliter(arr[mid:]))
        return spliter(nums)
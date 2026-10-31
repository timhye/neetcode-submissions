class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            if not left:
                return right
            elif not right:
                return left
            else:
                i, j = 0,0
                merged = []
                while i < len(left) and j < len(right):
                    if left[i] <= right[j]:
                        merged.append(left[i])
                        i += 1
                    else:
                        merged.append(right[j])
                        j += 1
                
                if i >= len(left):
                    while j < len(right):
                        merged.append(right[j])
                        j += 1
                elif j >= len(right):
                    while i < len(left):
                        merged.append(left[i])
                        i += 1
                
                return merged
        def split(arr):
            if len(arr) <= 1:
                return arr
            
            else:
                half = len(arr) // 2
                left = split(arr[:half])
                right = split(arr[:half])
            
            return merge(left, right)

        return split(nums)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        check = -1
        for num in range(len(matrix)):
            if matrix[num][0] <= target:
                check = num
        
        if check == -1:
            return False
        

        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            mid = left + (right - left + 1) // 2
            if matrix[check][mid] == target:
                return True
            elif matrix[check][mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1
            
        return False


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.store = [[0] * (len(matrix[0]) + 1) for n in range(len(matrix) + 1)]
        print(self.store)
        for i in range(1, len(self.store)):
            for j in range(1, len(self.store)):
                self.store[i][j] = matrix[i - 1][j - 1] + self.store[i][j - 1] + self.store[i - 1][j] - self.store[i - 1][j - 1]
        print(self.store)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.store[row2 + 1][col2 + 1] - self.store[row1][col2 + 1] - self.store[row2 + 1][col1]  + self.store[row1][col1] 
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
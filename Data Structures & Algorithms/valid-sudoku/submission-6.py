class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxs = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    box = (row // 3, col // 3)
                    if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in boxs[box]:
                        return False
                    else:
                        rows[row].add(board[row][col])
                        cols[col].add(board[row][col])
                        boxs[box].add(board[row][col])
        
        return True
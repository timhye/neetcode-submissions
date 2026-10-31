class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(list)
        rows = defaultdict(list)
        boxs = defaultdict(list)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    r, c = row // 3, col // 3
                    if board[row][col] in rows[row]:
                        return False
                    elif board[row][col] in cols[col]:
                        return False
                    elif board[row][col] in boxs[(r,c)]:
                        return False
                    else:
                        rows[row].append(board[row][col])
                        cols[col].append(board[row][col])
                        boxs[(r,c)].append(board[row][col])
        
        return True
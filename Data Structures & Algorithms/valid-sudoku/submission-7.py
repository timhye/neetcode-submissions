class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)
        value = 0
        for row in range(9):
            for col in range(9):
                
                if board[row][col]:
                    box = (row // 3, col // 3)
                    value = board[row][col]
                    if value in rows[row] or value in cols[col] or value in boxs[box]:
                        return False
                    else:
                        rows[row].add(board[row][col])
                        cols[col].add(board[row][col])
                        boxs[box].add(board[row][col])

        return True


                

                
                
                    



        
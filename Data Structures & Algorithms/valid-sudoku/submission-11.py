class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)
        value = 0
        for row in range(9):
            for col in range(9):

                if board[row][col] != ".":
                    box = (row // 3, col // 3)
                    value = board[row][col]
                    if value in rows[row] or value in cols[col] or value in boxs[box]:
                        print(value, row, col, box)
                        
                        return False
                    else:
                        rows[row].add(value)
                        cols[col].add(value)
                        boxs[box].add(value)

        return True


                

                
                
                    



        
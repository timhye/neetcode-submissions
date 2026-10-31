class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        row, col = 0, 0

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val != ".":
                    checkrow = row // 3
                    checkcol = col // 3
                    box = (checkrow, checkcol)
                
                    if val in rows[row] or val in cols[col] or val in boxes[box]:
                        return False
                        
                        
                    rows[row].add(val)
                    cols[col].add(val)
                    boxs[box].add(val)
        
        return True


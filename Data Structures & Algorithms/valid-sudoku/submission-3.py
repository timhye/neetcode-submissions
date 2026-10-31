class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        boxes = defaultdict(list)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                else:
                    if board[row][col] in rows[row]:
                        return False
                    if board[row][col] in cols[col]:
                        return False
                    r, c = row//3, col //3
                    if board[row][col] in boxes[(r,c)]:
                        return False
                
                rows[row].append(board[row][col])
                cols[col].append(board[row][col])
                boxes[(r,c)].append(board[row][col])
                    
        return True
                    



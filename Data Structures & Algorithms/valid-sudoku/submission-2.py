class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for digit in row:
                if (digit in seen) and (digit != "."):
                    return False
                else:
                    seen.add(digit)

        for i in range(9):
            seen = set()
            for j in range(9):
                if (board[j][i] in seen) and (board[j][i]!="."):
                    return False
                else:
                    seen.add(board[j][i])

        for square in range(9):
            seen = set() 
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3 + i
                    col = (square%3)*3 + j
                    if (board[row][col] in seen) and (board[row][col]!="."):
                        return False
                    else:
                        seen.add(board[row][col])
        
        return True

        
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols, anti_diag, diag = set(), set(), set()
        def isValid(row, col):
            return col not in cols and (row-col) not in diag and (row+col) not in anti_diag
        
        def helper(row):
            if row == n:
                temp = []
                for rowB in board:
                    temp.append("".join(rowB))
                res.append(temp)
                return
            
            for col in range(n):
                if isValid(row,col):
                    board[row][col] = 'Q'
                    cols.add(col)
                    diag.add(row-col)
                    anti_diag.add(row+col)
                    helper(row+1)
                    board[row][col] = '.'
                    cols.remove(col)
                    diag.remove(row-col)
                    anti_diag.remove(row+col)
        
        helper(0)

        return res
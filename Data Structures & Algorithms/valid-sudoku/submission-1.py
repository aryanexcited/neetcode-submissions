class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                item = board[i][j]
                
                if item == '.':
                    continue

                for k in range(rows):
                    if k!=i and board[k][j] == item:
                        return False
                
                for k in range(cols):
                    if k!=j and board[i][k] == item:
                        return False


                box_row = (i//3)*3
                box_col = (j//3)*3

                for k in range(box_row, box_row + 3):
                    for l in range(box_col, box_col + 3):
                        if (k != i or l != j) and item == board[k][l]:
                            return False

        return True
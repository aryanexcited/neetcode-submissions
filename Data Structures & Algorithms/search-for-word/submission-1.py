class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        w = len(word)
        def ex(row, col, idx):
            if idx == w:
                return True
            if not( 0 <= row < n and 0 <= col < m):
                return False
            if board[row][col] == "#":
                return False
            if board[row][col] != word[idx]:
                return False
            
            temp = board[row][col]
            board[row][col] = "#"
            ans = any([ex(row+dr, col+dc, idx+1) for (dr, dc) in [(-1,0), (1,0), (0,-1), (0,1)]])
            board[row][col] = temp
            return ans

        for i in range(n):
            for j in range(m):
                if ex(i,j,0):
                    return True
        
        return False
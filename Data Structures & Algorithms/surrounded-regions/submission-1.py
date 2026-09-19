class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])

        safe = deque()
        for i in range(col):
            if board[0][i] == "O":
                board[0][i] = "#"
                safe.append((0,i))
            if board[row-1][i] == "O":
                board[row-1][i] = "#"
                safe.append((row-1,i))

        for j in range(row):
            if board[j][0] == "O":
                board[j][0] = "#"
                safe.append((j,0))
            if board[j][col-1] == "O":
                board[j][col-1] = "#"
                safe.append((j,col-1))
        
        def bfs():
            while safe:
                x, y = safe.popleft()
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and board[nx][ny] == "O":
                        board[nx][ny] = "#"
                        safe.append((nx,ny))
            
            for i in range(row):
                for j in range(col):
                    if board[i][j] == "O":
                        board[i][j] = "X"
                    elif board[i][j] == "#":
                        board[i][j] = "O"

        return bfs()
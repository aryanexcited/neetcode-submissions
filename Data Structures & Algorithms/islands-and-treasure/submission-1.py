class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        tq = deque()
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    tq.append((i,j))

        def bfs():    
            while tq:
                x,y = tq.popleft()
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 2147483647:
                        grid[nx][ny] = grid[x][y] + 1
                        tq.append((nx,ny))
        
        bfs()
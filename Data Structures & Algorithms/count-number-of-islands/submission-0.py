class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def dfs(x,y,grid):
            queue = deque([(x,y)])
            grid[x][y] = "#"
            while queue:
                nx,ny = queue.popleft()
                for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                    cordX = nx + dx
                    cordY = ny + dy
                    if 0<=cordX<row and 0<=cordY<col and grid[cordX][cordY] != "0" and grid[cordX][cordY] != "#":
                        grid[cordX][cordY] = "#"
                        queue.append((cordX,cordY))

        count = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    count +=1
                    dfs(i,j,grid)
                
                else:
                    continue
                
        return count
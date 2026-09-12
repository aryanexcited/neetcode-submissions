class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        area = 0
        def dfs(x: int, y:int, grid: List[List[int]]):
            queue = deque([(x,y)])
            grid[x][y] = 2
            Carea = 1
            while queue:
                nx, ny = queue.popleft()
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    cordX = nx + dx
                    cordY = ny + dy

                    if 0<=cordX<row and 0<=cordY<col and grid[cordX][cordY] != 2 and grid[cordX][cordY] != 0:
                        Carea += 1
                        queue.append((cordX,cordY))
                        grid[cordX][cordY] = 2
            return Carea

        for i in range(row):
            for j in range(col):
                CArea = 0
                if grid[i][j] == 1:
                    CArea = dfs(i,j,grid)
                    area = max(area,CArea)

        return area
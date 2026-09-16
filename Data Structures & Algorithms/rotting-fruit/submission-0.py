class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        start = []
        totalFresh = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    start.append((i,j))
                if grid[i][j] == 1:
                    totalFresh += 1

        def bfs():
            nonlocal totalFresh
            count = 0
            queue = deque(start)
            while queue:
                level_size = len(queue)
                workDone = False
                for _ in range(level_size):
                    x, y = queue.popleft()
                    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            queue.append((nx,ny))
                            totalFresh -= 1
                            workDone = True
                if workDone:
                    count += 1

            return count
        minute = bfs()
        minute = -1 if totalFresh else minute
        return minute
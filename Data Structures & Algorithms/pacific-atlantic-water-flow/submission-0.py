class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row = len(heights)
        col = len(heights[0])

        atlantic = deque()
        pacific = deque()
        for i in range(col):
            pacific.append((0,i))
            atlantic.append((row-1,i))

        for i in range(row):
            pacific.append((i,0))
            atlantic.append((i,col-1))

        def bfs(queue):
            ans = set()
            while queue:
                x, y = queue.popleft()
                ans.add((x,y))
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and (nx,ny) not in ans and heights[nx][ny] >= heights[x][y]:
                        ans.add((nx,ny))
                        queue.append((nx,ny))
                    
            return ans
        
        pacific_set = bfs(pacific)
        atlantic_set = bfs(atlantic)

        return [(r,c) for r,c in pacific_set & atlantic_set]
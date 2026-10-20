class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def bfs(point):
            q = deque([point])

            while q:

                curr_point = q.popleft()
                cx, cy = curr_point

                if curr_point in visited:
                    continue
                
                visited.add(curr_point)

                for x, y in DIRECTIONS:
                    nx = cx + x
                    ny = cy + y
                    if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == "1":
                        q.append((nx, ny))
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs((r, c))
                    res += 1
        return res
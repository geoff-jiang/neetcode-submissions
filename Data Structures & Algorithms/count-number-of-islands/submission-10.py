class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(r, c): 
            stack = []
            stack.append((r, c))

            while stack:
                cr, cc = stack.pop()

                for x, y in directions:
                    nx = x + cr
                    ny = y + cc
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == "1":
                        stack.append((nx, ny))
                        visited.add((nx, ny))

            return 1

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    visited.add((r, c))
                    res += bfs(r, c)
        return res

            

                            


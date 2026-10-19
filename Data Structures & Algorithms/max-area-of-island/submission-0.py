class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        visited = set()

        def dfs(r, c):
            
            if (r, c) in visited or r not in range(rows) or c not in range(cols) or grid[r][c] != 1:
                return 0
            
            visited.add((r, c))

            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

            return (1 + dfs(r + 1, c) + dfs(r -1, c) + dfs(r, c + 1) + dfs(r, c -1))
                    
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(dfs(r, c), res)
              
        return res
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        visited = set()

        def dfs(r ,c):
            if (r, c) in visited:
                return
            
            visited.add((r, c))
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for x, y in directions: 
                new_row = r + x
                new_col = c + y
                if new_row in range(rows) and new_col in range(cols) and grid[new_row][new_col] == "1":
                    dfs(new_row, new_col)
            
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
                
        return res
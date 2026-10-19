class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        def bfs(r, c):
            q = deque()
            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

            if (r,c) in visited: 
                return 0

            q.append((r, c))
            visited.add((r, c))
            while q:
                x1, y1 = q.popleft()    
                for x, y in directions: 
                    if x1 + x in range(rows) and y1 + y in range(cols) and grid[x1 + x][y1 + y] == "1" and (x1 + x, y1 + y) not in visited:
                        q.append((x1 + x, y1 + y))
                        visited.add((x1+x, y1 + y))
            return 1

            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += bfs(r, c)

        return res
                

            

                            


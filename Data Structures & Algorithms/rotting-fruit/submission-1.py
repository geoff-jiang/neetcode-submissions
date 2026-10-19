class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        res = 0

        dq = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    dq.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        while dq:
            if fresh == 0: break
            res += 1
            for i in range(len(dq)):
                r, c = dq.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for x, y in directions:
                    nr = r + x
                    nc = c + y
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        dq.append((nr, nc))
                        fresh -= 1
            
        
        return res if fresh == 0 else -1
            

            
                
                


        

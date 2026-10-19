class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        res = 0

        q = deque()
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                if grid[row][col] == 1:
                    fresh += 1
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
 
                for x, y in directions:
                    nr = x + r
                    nc = y + c
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            res += 1
            
        return res if fresh == 0 else -1
            

            
                
                


        

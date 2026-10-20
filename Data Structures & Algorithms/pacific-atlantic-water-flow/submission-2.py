class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # memoize with dictionary of {(point): boolean} for early returns. 
        # bfs on each node, if 2 nodes in the queue reach oceans, then return true.
        # edge cases: one cell - return True
        # no negative numbers

        ROWS = len(heights)
        COLS = len(heights[0]) 
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        res = []
        
        def bfs(point):
            q = deque([point])

            touchAtlantic = False
            touchPacific = False

            visited = set()
            
            while q: 
                curr = q.popleft()
                cx, cy = curr

                if curr in visited:
                    continue
                visited.add(curr)

                if cx == 0 or cy == 0:
                    touchPacific = True
                if cy == COLS -1 or cx == ROWS - 1:
                    touchAtlantic = True

                if touchAtlantic and touchPacific: 
                    return True
                
                for x, y in DIRECTIONS:
                    nx = x + cx
                    ny = y + cy
                    if 0 <= nx < ROWS and 0 <= ny < COLS and heights[nx][ny] <= heights[cx][cy]:
                        q.append((nx ,ny))
            return touchAtlantic and touchPacific
        
        for r in range(ROWS):
            for c in range(COLS):
                if bfs((r, c)):
                    res.append([r, c])
        return res


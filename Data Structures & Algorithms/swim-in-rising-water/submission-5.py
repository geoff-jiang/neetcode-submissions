class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # dfs 
        # store max of each path
        # return minimum of the path max's 

        ROWS, COLS = len(grid), len(grid[0])
        END = (ROWS - 1, COLS - 1)

        heap = [(grid[0][0], (0, 0))]
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while heap:
            maxOnPath, point = heapq.heappop(heap)

            if point in visited:
                continue
            visited.add(point)

            if point == END:
                return maxOnPath

            x, y = point
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (
                    0 <= nx < ROWS
                    and 0 <= ny < COLS
                    and (nx, ny) not in visited
                ):
                    cost = max(maxOnPath, grid[nx][ny])
                    heapq.heappush(heap, (cost, (nx, ny)))


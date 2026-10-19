class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # djikstra's 
        # visited set so we don't process duplicate point
        # keep track of total connection cost (passed into the heap)
        # end loop when visited set == total points

        
        heap = [(0, tuple(points[0]))]
        # (currentCost, point) 
        visited = set()

        dist = {tuple(points[0]): 0}
        # keep track of point and its cloest neighbor distance {[0, 0]: 4}
        
        total = 0
        while heap: 
            cost, point = heapq.heappop(heap)
            if point in visited: 
                continue
            
            visited.add(point)
            total += cost

            x, y = point

            for nx, ny in points: 

                neighbor = (nx, ny)
                if neighbor in visited:
                    continue
                manDist = abs(nx - x) + abs(ny - y)
                if manDist < dist.get(neighbor, float('inf')):
                    dist[neighbor] = manDist
                    heapq.heappush(heap, (manDist, neighbor))
        
        return total


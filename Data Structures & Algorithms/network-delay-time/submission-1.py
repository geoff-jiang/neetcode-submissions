class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dikstras
        # visited set checking if length = total nodes
        # store total time in heap

        adjList = defaultdict(list) 
        for ui, vi, ti in times:
            adjList[ui].append((vi,ti))
        
        # {1: [(2, 1), (4, 4]}
        
        distances = defaultdict(lambda: float('inf')) # need to populate with infinity? 
        distances[k] = 0
        # (4: minTime) 
        heap = [(0, k)]
        # (path, node)

        visited = set() # pass into heap?

        while heap:
            path, node = heapq.heappop(heap)
            neighbors = adjList[node]
            if node in visited: 
                continue

            visited.add(node)

            if len(visited) == n:
                return path
                
            for dest, weight in neighbors: 
                if distances[dest] > path + weight:
                    distances[dest] = path + weight
                    heapq.heappush(heap, (path + weight, dest))
            
        return -1




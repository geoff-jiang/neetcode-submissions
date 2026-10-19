class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        heap = [(0, src, 0)]
        # cost, airport, stops

        adjList = defaultdict(list)

        for start, stop, cost in flights: 
            adjList[start].append((stop, cost)) 
        # {1: [2, 3]}

        visited = set()

        while heap: 
            cost, airport, stops = heapq.heappop(heap)

            temp = (airport, stops)

            if temp in visited or stops > k + 1:
                continue

            visited.add(temp) 

            if airport == dst: 
                return cost
            
            for dest, weight in adjList[airport]:
                heapq.heappush(heap, (cost + weight, dest, stops + 1))

        return -1

                
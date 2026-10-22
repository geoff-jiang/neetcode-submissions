class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # djikstra's algorithm
        # build adjacency list
        adjList = defaultdict(list)
        for s, d, p in flights:
            adjList[s].append((d, p))
    
        # keep track of shortest path to airport with k flights in a dict
        distances = {(src, 0): 0}
        # append starting airport to the queue
        # heap contains (price, src, k)
        heap = [(0, src, 0)]
        while heap:
            cost, curr, kleft = heapq.heappop(heap)
            
            if curr == dst:
                return cost
            if kleft >= k + 1:
                continue

        # always enqueue the shortest neighbor
            for dest, price in adjList[curr]:
                if cost + price < distances.get((dest, kleft + 1), float('inf')):
                    heapq.heappush(heap, (cost + price, dest, kleft + 1))
                    distances[(dest, kleft + 1)] = cost + price
        # queue neighbors that can be reached cheaper than current cheapest path 
        # start with infinity
        # if numStops > k, break (store k in queue)
        return -1



    
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        distances = []
        heapq.heapify(distances)
        for x, y in points: 
            distance = -(x**2 + y**2)
            heapq.heappush(distances, [distance, x, y])
            if len(distances) > k:
                heapq.heappop(distances)
        
        for i in range(k):
            distance, x, y = heapq.heappop(distances)
            res.append([x, y])
        return res
            
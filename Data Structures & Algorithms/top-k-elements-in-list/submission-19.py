import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a minheap of size k 
        lib = Counter(nums)
        heap = []
        for i, v in lib.items():
            heapq.heappush(heap, (v, i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for v, i in heap:
            res.append(i)
        return res

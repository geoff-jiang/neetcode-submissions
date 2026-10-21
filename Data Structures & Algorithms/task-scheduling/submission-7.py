class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count number of occurecnces of each tast
        # heapify them
        # keep popping most frequent task
        # send them into a queue with a timer, and num remaning tasks
        # pop back in whe time reaches

        count = Counter(tasks)
        # {'X': 2, 'Y': 2}
        # heap: [1]
        # q: [(4, 1)]
        # time: 4

        heap = []
        for c in count.values():
            heapq.heappush(heap, -c)
        
        q = deque()
        time = 0

        while heap or q: 
            time += 1
            if heap: 
                curr = heapq.heappop(heap)
                curr += 1
                if curr < 0:
                    q.append((time + n, curr))
            
            if q and q[0][0] == time: 
                    needed, left = q.popleft()
                    heapq.heappush(heap, left)
        
        return time


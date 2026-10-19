class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskMap = defaultdict(int)
        for t in tasks: 
            taskMap[t] += 1
        maxHeap = []
        for v in taskMap.values():
            maxHeap.append(v * -1)
        heapq.heapify(maxHeap)

        q = deque()
        time = 0
        while maxHeap or q:
            print(maxHeap)
            print(q)
            time += 1
            if maxHeap:
                cur = heapq.heappop(maxHeap)
                cur += 1
                if cur < 0:
                    q.append([cur, time + n])

            if q and q[0][1] == time:
                freq, time = q.popleft()
                heapq.heappush(maxHeap, freq)
        return time
                


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort the intervals by start time
        # dictionary storing values with start and times
        # start 1: + 1
        # 3: -1
        # 2: + 1
        # dictionary with start and end
        

        intervals.sort(key = lambda x : x.start)

        res = 0
        heap = []

        for i in intervals:
            if heap and heap[0] <= i.start:
                heapq.heappop(heap)
            heapq.heappush(heap, i.end)
            res = max(res, len(heap))
        return res


        # timeDict = defaultdict(int)

        # maxEnd = 0
        # for i in intervals:
        #     maxEnd = max(maxEnd, i.end)
        #     timeDict[i.start] += 1
        #     timeDict[i.end] -= 1

        # res = 0
        # counter = 0
        # for i in range(maxEnd):
        #     if i in timeDict:
        #         counter += timeDict[i]
        #         res = max(res, counter)
        
        # return res
    
        





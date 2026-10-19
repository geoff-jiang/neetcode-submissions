"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes = []
        endTimes = []
        for i in intervals:
            startTimes.append(i.start)
            endTimes.append(i.end)
        startTimes.sort()
        endTimes.sort()
       
        s = 0
        e = 0
        
        res = 0
        count = 0

        while s < len(startTimes):
            if startTimes[s] < endTimes[e]:
                count += 1
                s += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res


        
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_arr = sorted([i.start for i in intervals])
        end_arr = sorted([i.end for i in intervals])
        s, e = 0, 0
        curr, res = 0, 0

        while s < len(intervals):
            if start_arr[s] < end_arr[e]:
                s += 1
                curr += 1
            else:
                e += 1
                curr -= 1
            res = max(res, curr)

        return res

        
        



class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy approach: when overlap occurs, take the interval with a smaller end time. 
        # count the number of intervals removed
        # inversion: flip the goal (minimum removed = max kept! )
        res = -1

        intervals.sort(key=lambda x: x[0])

        print(intervals)

        currEnd = intervals[0][1]

        for start, end in intervals:
            if start >= currEnd:
                currEnd = end
            else:
                currEnd = min(currEnd, end)
                res += 1
        return res





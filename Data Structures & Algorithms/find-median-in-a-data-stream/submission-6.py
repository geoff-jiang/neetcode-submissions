class MedianFinder:

    def __init__(self):
        self.smaller, self.larger = [], []

    def addNum(self, num: int) -> None:
        if self.larger and num > self.larger[0]:
            heapq.heappush(self.larger, num)
        else: 
            heapq.heappush(self.smaller, num * -1)
        
        if len(self.smaller) > len(self.larger) + 1: 
            temp = heapq.heappop(self.smaller) * -1
            heapq.heappush(self.larger, temp)
        elif len(self.larger) > len(self.smaller) + 1: 
            temp = heapq.heappop(self.larger) * -1
            heapq.heappush(self.smaller, temp)

        

    def findMedian(self) -> float:
        if len(self.smaller) > len(self.larger):
            return -1 * self.smaller[0]
        elif len(self.larger) > len(self.smaller):
            return self.larger[0]
        else: 
            return (self.larger[0] + (self.smaller[0] * -1)) / 2
        
        
class MedianFinder:

    def __init__(self):
        self.smallHeap, self.bigHeap = [], []
        

    def addNum(self, num: int) -> None:
        if self.bigHeap and num > self.bigHeap[0]:
            heapq.heappush(self.bigHeap, num)
        else:
            heapq.heappush(self.smallHeap, num * -1)
        
        if len(self.bigHeap) > len(self.smallHeap) + 1:
            top = heapq.heappop(self.bigHeap) * -1
            heapq.heappush(self.smallHeap, top)
        elif len(self.smallHeap) > len(self.bigHeap) + 1:
            top = heapq.heappop(self.smallHeap) * -1
            heapq.heappush(self.bigHeap, top)


    def findMedian(self) -> float:
        if len(self.bigHeap) == len(self.smallHeap):
            return float((self.bigHeap[0] + self.smallHeap[0] * -1) / 2.0)
        elif len(self.bigHeap) > len(self.smallHeap):
            return float(self.bigHeap[0])
        else:
            return float(self.smallHeap[0] * -1)
        
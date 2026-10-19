class MedianFinder:

    def __init__(self):
        self.arr = []
        self.left = -1
        self.right = 0
        self.even = True

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        self.even = not self.even
        if not self.even:
            self.left += 1
            self.right += 1
        
    def findMedian(self) -> float:
        if self.even: 
            return float((self.arr[self.left] + self.arr[self.right]) / 2)
        else:
            return self.arr[self.left]
        
        
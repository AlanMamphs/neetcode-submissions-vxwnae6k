class MedianFinder:

    def __init__(self):
        self.min_h = []
        self.max_h = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_h, num)
  
        while self.max_h and -self.max_h[0] > self.min_h[0]:
            heapq.heappush(self.max_h, -heapq.heappop(self.min_h))
            heapq.heappush(self.min_h, -heapq.heappop(self.max_h))
        while (len(self.min_h) - len(self.max_h)) > 1:
            heapq.heappush(self.max_h, -heapq.heappop(self.min_h))

    def findMedian(self) -> float:
        if not self.min_h:
            return None
        if (len(self.min_h) + len(self.max_h)) % 2:
            return self.min_h[0]
        else:
            return (self.min_h[0] - self.max_h[0]) / 2
class MedianFinder:

    def __init__(self):
        self.smaller = []
        self.larger = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smaller,-num)
        popVal = -(heapq.heappop(self.smaller))
        heapq.heappush(self.larger, popVal)
        if len(self.larger) > len(self.smaller):
            popVal = heapq.heappop(self.larger)
            heapq.heappush(self.smaller, -popVal)

    def findMedian(self) -> float:        
        if len(self.smaller) > len(self.larger):
            return -self.smaller[0]
        
        else:
            return (-self.smaller[0]+self.larger[0])/2
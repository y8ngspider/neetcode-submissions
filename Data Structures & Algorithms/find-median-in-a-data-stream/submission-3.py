class MedianFinder:

    def __init__(self):
        self.maxleft = []
        self.minright = []

    def addNum(self, num: int) -> None:
        if self.minright and num > self.minright[0]:
            heapq.heappush(self.minright,num)
        else:    
            heapq.heappush_max(self.maxleft,num)

        if len(self.maxleft) - len(self.minright) >= 2:
            n = heapq.heappop_max(self.maxleft)
            heapq.heappush(self.minright,n)
        elif len(self.minright) - len(self.maxleft) >= 2:
            n = heapq.heappop(self.minright)
            heapq.heappush_max(self.maxleft,n)

    def findMedian(self) -> float:
        if len(self.maxleft) > len(self.minright):
            return float(self.maxleft[0])
        elif len(self.minright) > len(self.maxleft):
            return float(self.minright[0])
        else:
            return (self.maxleft[0] + self.minright[0])/2
        
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max-Heap (Left) - minus pottu store pannuvom
        self.large = []  # Min-Heap (Right)

    def addNum(self, num: int) -> None:
        # 1. First large la podu, aprom small ku balance pannu
        heapq.heappush(self.small, -num)
        
        # Small oda top perusa irundha, large ku anuppu
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Size balance: small perusa irundha, large ku anuppu
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Large perusa irundha, small ku anuppu
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
class MedianFinder:

    # Our approach: Heaps
    # Maintain 2 heaps: one for smaller half and one for larger half
    # Median will simply be the max of smaller half and min of lower half / 2.
    # Hence, first half is a maxHeap and second half is minHeap
    # By default, we push to the smaller half. 
    # If heaps are of equal size, push to maxHeap, then pop from maxHeap and push to minHeap
    # Else, if minHeap has more elements, push there, then pop and add to maxHeap
    # This way, we ensure that the difference between heaps is at max 1


    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == len(self.minHeap):
            heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, -num))
        else:
            heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap, num))

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return float(self.minHeap[0] - self.maxHeap[0]) / 2
        else:
            return float(self.minHeap[0])        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

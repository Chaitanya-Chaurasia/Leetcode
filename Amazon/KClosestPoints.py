class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # Trick: Use Min Heap
        # Push the negative of distance into the heap
        # Pop the heap k times.

        heap, res = [], []
        
        for x, y in points:
            dist = sqrt(x*x + y*y)
            heapq.heappush(heap, (dist, [x, y]))

        
        res = []
        for _ in range(k):
            dist, point = heapq.heappop(heap)
            res.append(point)
        return res
        

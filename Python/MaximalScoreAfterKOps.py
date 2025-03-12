class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        # Approach: Max Heap
        # Since heapq is by default a minheap, we negate the values to keep track of max value
        # Maintain a max heap, and keep popping the max elements until k operations are done.

        heap = [-i for i in nums]
        heapq.heapify(heap)
        
        maxScore = 0
        while k > 0:
            maxElement = -heapq.heappop(heap)
            maxScore += maxElement
            heapq.heappush(heap, -math.ceil(maxElement/3))
            k -= 1
        
        return maxScore

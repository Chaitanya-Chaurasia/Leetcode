class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        # easy approach would be min heap
        # since every row is sorted, we can use heap to find the minimum element.
        # since every column is also sorted, if k < no of rows, we only need to search until k rows.
        # we can start by pushing the first elements of each row.
        # if we're still not at kth smallest, we add the next element of the row and move to the next.

        rows, cols = len(matrix), len(matrix[0])
        heap = []
        count, kth_smallest = 0, 0

        for i in range(min(rows, k)):
            heapq.heappush(heap, (matrix[i][0], i, 0))
            
        while heap:
            kth_smallest, row, col = heapq.heappop(heap)
            count += 1

            if count == k:
                break
            
            if col + 1 < cols:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
            
        return kth_smallest 

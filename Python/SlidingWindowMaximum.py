class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # Our approach: Use a double-ended queue and enque and deque
        # This will give TLE
        
        # queue = deque(nums[:k])
        # maxSlidingWindow = [max(queue)]

        # for right in nums[k:]:
        #     queue.popleft()
        #     queue.append(right)
        #     maxSlidingWindow.append(max(queue))

        # return maxSlidingWindow

        # Approach 2: Using Heap
        heap = []
        maxSlidingWindow = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        
        maxSlidingWindow.append(-heap[0][0])

        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            
            maxSlidingWindow.append(-heap[0][0])

        return maxSlidingWindow

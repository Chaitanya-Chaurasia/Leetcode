class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        maxSum = window_sum = sum(nums[:k])
        

        # to optimize solution, store the value of first window, and start iterating from k+1th element
        # iterate over nums and keep on adding right element, and deleting left element.

        for i in range(k, len(nums)):
            window_sum += -nums[i - k] + nums[i]
            maxSum = max(maxSum, window_sum)
            
        return maxSum/k

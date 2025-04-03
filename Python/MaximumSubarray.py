class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0] 

        # Our approach: Kadane's Algorithm
        # Start from the first element and expand subarray and record sum
        # Update the subarray if the sum of new subarray is less than old subarray. 

        subarray, res, n = nums[0], nums[0], len(nums)

        for i in range(1, n):
            # Either two possibilites:
            # nums[i] itself is greater than the previous maxSubarray,and marks the start of a new subarray.
            # maxSum + nums[i] > nums[i] and hence we include it in our subarray.
            subarray = max(subarray + nums[i], nums[i])
            res = max(res, subarray)
        return res

        # Two Pointer solutions
        # Our approach: for every time we increment the right window, if the sum is negative
        # iterate over elements to remove all negative elements from left.

        # maxSum = currSum = nums[0]
        # left = 0
        # for right in range(1, len(nums)):
        #     currSum += nums[right]
        #     maxSum = max(currSum, maxSum)
        #     while currSum < 0:
        #         currSum -= nums[left]
        #         left += 1
        # return maxSum

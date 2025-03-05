class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0] 

        # Our approach: Kadane's Algorithm
        # Start from the first element and expand subarray and record sum
        # Update the subarray if the sum of new subarray is less than old subarray. 

        # maxSum = ans = nums[0]
        # for i in range(1, len(nums)):
        #     maxSum = max(maxSum + nums[i], nums[i])
        #     ans = max(ans, maxSum)
        # return ans

        # Two Pointer solutions
        # Our approach: for every time we increment the right window, if the sum is negative
        # iterate over elements to remove all negative elements from left.

        maxSum = currSum = nums[0]
        left = 0
        for right in range(1, len(nums)):
            currSum += nums[right]
            maxSum = max(currSum, maxSum)
            while currSum < 0:
                # print("here: " , currSum)
                currSum -= nums[left]
                left += 1
        return maxSum

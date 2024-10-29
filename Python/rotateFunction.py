class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        # our approach
        # for these questions, find a mathematical formula that can satisfy our relation
        # turns out, when you subtract F(k) and F(k-1), the relation is that
        # F(k) = F(k-1) + sum - (n-1)*(k - 1)th element

        # dp = [0]*len(nums)
        # dp[0] = sum(i*nums[i] for i in range(len(nums)))
        # l, s = len(nums), sum(nums)

        # if len(nums) == 1: return 0

        # for i in range(1, len(nums)):
        #     dp[i] += dp[i - 1] + s - l * nums[l - i]
        # return max(dp)

        # this uses extra memory and we can optimize this further
        F_i = sum(i * j for i, j in enumerate(nums))
        maxF = F_i
        l, s = len(nums), sum(nums)

        if len(nums) == 1:
            return 0
        
        for i in range(1, l):
            F_i += s - l * nums[l - i ]
            maxF = max(maxF, F_i)
        return maxF

class Solution:
    def maxProfit(self, nums: List[int]) -> int:

        min = nums[0]
        max = 0

        for i in nums:
            if i < min:
                min = i

            profit = i - min

            if profit > max:
                max = profit

        return max


        

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # TRICK: Calculate the profit between consecutive days
        # Then simply find maximum subarray sum to check which range has max profit

        n = len(prices)
        profit, subarraySum = 0, 0

        for i in range(0, n - 1):
            prices[i] = prices[i + 1] - prices[i]
        
        # We do this because we only interated over (0, n - 1) leaving the last element unchanged.
        # But since we accounted for the profit in prices[n - 1], we put it as zero.
        
        prices[-1] = 0

        for i in range(1, n):
            subarraySum = max(subarraySum + prices[i], prices[i])
            profit = max(subarraySum, profit)
        
        return profit

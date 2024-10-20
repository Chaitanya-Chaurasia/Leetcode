class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        first, second = cost[0], cost[1]
        l = len(cost)
        if l <= 2:
            return min(first, second)
        
        for i in range(2, l):
            cost_to_stair_i = cost[i] + min(first, second)
            first = second
            second = cost_to_stair_i
        
        return min(first, second)

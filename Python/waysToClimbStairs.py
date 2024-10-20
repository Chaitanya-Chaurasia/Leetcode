class Solution:
    def climbStairs(self, n: int) -> int:
        
        # dp function is ways = ways[i] + ways[i - 2]
        first, second = 1, 1
        ways = 2

        if n == 1:
            return first

        if n == 2:
            return first + second

        for i in range(2, n + 1):
            ways = first + second
            first = second
            second = ways

        return ways
        


        

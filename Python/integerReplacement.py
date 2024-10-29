class Solution:
    def integerReplacement(self, n: int) -> int:

        def helper(val):
            if val == 1:
                return 0

            if val%2 == 0:
                return 1 + helper(val/2)
            else:
                return min(1 + helper(val + 1), 1 + helper(val - 1))
        
        return helper(n)

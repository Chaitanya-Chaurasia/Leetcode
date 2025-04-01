class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        # Our approach: Backtracking
        # This is similar to CombSum I, except that we need to determine where to start iterating from
        # Our loop will iterate from either 1, if comb is empty or comb[-1].
        # We only backtrack if sum is less than n.

        combinations = []

        def backtrack(total, comb):
            if len(comb) == k:
                if total == n:
                    combinations.append(comb[:])
                return
            
            start = 1 if not comb else comb[-1] + 1
            for i in range(start, 10):
                if total + i <= n:
                    comb.append(i)
                    backtrack(total + i, comb)
                    comb.pop()

        backtrack(0, [])
        return combinations

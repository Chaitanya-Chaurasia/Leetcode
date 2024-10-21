class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []

        def backtrack(idx, combination, total):
            if len(combination) == k:
                if total == n:
                    res.append(combination)
                return
            
            for i in range(idx, 10):
                current_sum = total + i
                if current_sum <= n:
                    backtrack(idx + 1, combination + [i], current_sum)
        
        backtrack(1, [], 0)
        return res

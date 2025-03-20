class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # Trick: Sort array to avoid duplicates and skip over them like in 3Sum
        result, combination = [], []
        candidates.sort()

        def backtrack(start):
            if sum(combination) == target:
                result.append(combination[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] + sum(combination) > target:
                    break

                combination.append(candidates[i])
                backtrack(i + 1)
                combination.pop()

        backtrack(0)
        return result
        

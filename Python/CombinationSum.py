class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # our approach - recursion (backtracking)
        # for every candidates[i],  we will recursively check for all different decisions paths that can occur
        # sort of like DFS. To avoid duplicates, we will ensure that at at every decision node, we will choose two
        # distinct paths. This will ensure that one combination will only occur once.
        # base case would be if we're at the last element or if total sum is equal to target
        
        combinations = []
        def dfs(i, currentCombination, total):
            if total == target:
                combinations.append(currentCombination[:])
                return
            
            if total > target or i >= len(candidates):
                return
            
            currentCombination.append(candidates[i])
            dfs(i, currentCombination, total + candidates[i])

            currentCombination.pop()
            dfs(i + 1, currentCombination, total)

        dfs(0, [], 0)
        return combinations

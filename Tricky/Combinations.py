class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # Our approach: Backtracking
        # We define a helper method called backtrack(start).
        # We know that the length of each combination has to be k.
        # So we will keep on appending to our combination array until comb is our length k.
        # Once that is done, we have one such combination. We then remove last element from our array, and 
        # add the next element since we are iterating. 

        combination, result = [], []

        def backtrack(start):
            if len(combination) == k:
                result.append(combination[:])
                return
            
            for i in range(start, n + 1):
                combination.append(i)
                backtrack(i + 1)
                combination.pop()

        backtrack(1)
        return result

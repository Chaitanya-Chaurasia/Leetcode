class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # TRICK: Difference b/w combinations and permutations.
        # For permutation, order doesn't matter i.e any element can be picked.
        # For combination, order matters and we have to pick elements in order. 
        # For this question, we need to keep track of built permutation as well as remaining elements
        # we can use to build a permutation

        result = []

        def backtrack(perm, remaining):
            if not remaining:
                result.append(perm[:])
                return
            
            for i in range(len(remaining)):
                perm.append(remaining[i])
                backtrack(perm, remaining[:i] + remaining[i+1:])
                perm.pop()
            
            # THERE IS A DIFFERNCE BETWEEN 
            # for i in range(len(remaining)):     
            #     backtrack(perm + [remaining[i]], remaining[:i] + remaining[i+1:])

            # and 
            # for i in range(len(remaining)):
            #     perm.append(remaining[i])
            #     backtrack(perm, remaining[:i] + remaining[i+1:])


            # In the first approach, we make a new list using perm + [remaining[i]].
            # In every iteration, we create a new list.
            # But in the second iteration, we modify the original list. Which is why we need to pop()
            # at the end to get the original list back 
            
        backtrack([], nums)
        return result

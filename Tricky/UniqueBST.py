class Solution:
    def numTrees(self, n: int) -> int:

        # Naive approach: Recursion
        # Con: 0(4^n) and TLE for larger numbers.
        # Need to break into subproblems.
        # def generateTrees(start, end):
        #     if start > end:
        #         return [None, ]
            
        #     trees = []
        #     for i in range(start, end + 1):
        #         left = generateTrees(start, i - 1)
        #         right = generateTrees(i + 1, end)            

        #         for l in left:
        #             for r in right:
        #                 newTree = []
        #                 newTree.append(left)
        #                 newTree.append(right)
        #                 trees.append(newTree)
        #     return trees

        # return len(generateTrees(1, n)) if n > 1 else 1
        
        # New Approach: Dynamic Programming
        # We maintain a memo where memo[i] stores the number of trees with i as root.
        # The total number of trees possible with n elements at left and m elements at right is n*m. 
        # We add this to the cache, and simply return memo[n]

        memo = [1] * (n + 1)
        
        for root in range(2, n + 1):
            total = 0
            for left in range(1, root + 1):
                right = root - left
                # left - 1 because if root is 3, left will contain left - 1 i.e 3 - 1 = 2 elements
                total += memo[left - 1] * memo[right]
            memo[root] = total
        return memo[n] 

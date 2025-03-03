class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # Simple backtracking approach
        # We want to have a DFS approach where for every left pair of parantheses, we will look for
        # all the options available. 
        # Base case will be when the length of our string is 2*n.
        res = []
        def dfs(l, r, combination):
            if len(combination) == 2 * n:
                res.append(combination)
            
            if l < n:
                dfs(l + 1, r, combination + "(")
            if l > r:
                dfs(l, r + 1, combination + ")")

        dfs(0, 0, "")
        return res

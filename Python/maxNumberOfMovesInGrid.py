class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        # our approach is start with every value in the first column
        # for every element, do a dfs
        # maintain a memo table that stores the moves to a particular row,col
        # we do this to avoid computing multiple times in case a certain grid val is accessible via multiple routes
        # tip, use @cache to use auto memoization

        row, col = len(grid), len(grid[0])
        directions, memo, res = [(-1, 1), (0, 1), (1, 1)], {}, 0
        def dfs(i, j):
            # base cases
            if j == col - 1:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            moves = 0
            for x, y in directions:
                new_i, new_j = i + x, j + y
                if 0 <= new_i < row and 0 < new_j < col and grid[new_i][new_j] > grid[i][j]:
                    moves = max(moves, 1 + dfs(new_i, new_j))
            memo[(row, col)] = moves
            return moves

        for i in range(row):
            res = max(res, dfs(i, 0))
        
        return res

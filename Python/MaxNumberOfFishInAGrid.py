class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        # Our approach: DFS
        # Run DFS on every non-zero cell. 
        # Keep track of visited nodes and number of fish on each DFS

        rows, cols = len(grid), len(grid[0])
        maxFish = 0

        def dfs(x, y):
            if x < 0 or y < 0 or x == rows or y == cols or grid[x][y] == 0:
                return 0
            fish = grid[x][y]
            grid[x][y] = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                fish += dfs(x + dx, y + dy)
            return fish
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    maxFish = max(maxFish, dfs(i, j))
        return maxFish

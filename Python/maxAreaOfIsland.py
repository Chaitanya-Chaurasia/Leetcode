class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # Our approach: DFS
        # Check for grid[i][j] == 1, and commence DFS from there.
        # Maintain a visited set so we don't count the same vertex twice.
        # Remove from the set once DFS has finished.
        # Keep track of area in a result

        maxArea = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        
        # RECURSIVE APPROACH
         def dfs(x, y):
            # since we want to visit an island only once, we can mark the coordinates as 0
            if x not in range(rows) or y not in range(cols) or grid[x][y] != 1:
                return 0
            grid[x][y] = 0
            area = 1
            area += dfs(x + 1, y)
            area += dfs(x - 1, y)
            area += dfs(x, y + 1)
            area += dfs(x, y - 1)
            return area

        # ITERATIVE APPROACH
        def dfs(x, y):
            # since we want to visit an island only once, we can mark the coordinates as 0
            grid[x][y] = 0
            area = 1
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if x + dx in range(rows) and y + dy in range(cols) and grid[x + dx][y + dy] == 1:
                    area += dfs(x + dx, y + dy)
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))

        return maxArea

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        # Our approach: DFS
        # Since we can only consider those islands that are also valid in grid1, 
        # we can start by removing all the land cells in grid2 that are water cells in grid1
        # This way, we shorten our searching area.
        # Once we've done this, we simply need to count the islands in grid2

        rows, cols = len(grid1), len(grid1[0])
        subIslands = 0
       
        def dfs(x, y):
            if x < 0 or y < 0 or x >= rows or y >= cols or grid2[x][y] == 0:
                return 

            grid2[x][y] = 0
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(x + dx, y + dy)

        for i in range(rows):
            for j in range(cols):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    dfs(i, j)

        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    subIslands += 1
                    dfs(i, j)
        
        return subIslands

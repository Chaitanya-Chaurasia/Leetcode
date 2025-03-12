class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        # Our approach: DFS
        # We need to do a 4 way DFS for every guarded cell, and keep going until 
        # we either hit another wall or guard
                
        grid = [["." for _ in range(n)] for _ in range(m)]

        def dfs(x, y, dx, dy):
            while 0 <= x < m and 0 <= y < n:
                if grid[x][y] in ["G", "W"]:
                    break
                grid[x][y] = "#"
                x += dx
                y += dy

        for x, y in guards:
            grid[x][y] = "G"
        for x, y in walls:
            grid[x][y] = "W"
        for x, y in guards:
            dfs(x, y + 1, 0, 1)
            dfs(x, y - 1, 0, -1)
            dfs(x + 1, y, 1, 0)
            dfs(x - 1, y, -1, 0)
            
        unguarded = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == ".":
                    unguarded += 1
        
        return unguarded

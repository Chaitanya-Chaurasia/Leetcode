class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        
        visited = set()
        islands = 0

        row , col = len(grid), len(grid[0])

        # def bfs(i, j):

        #     visited.add((i,j))
        #     neighbour_coordinates = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        #     for x, y in neighbour_coordinates:
        #         if i + x in range(row) and j + y in range(col) and grid[i][j] == "1" and (i + x, j + y) not in visited:
        #             bfs(i + x, y + j)
        neighbour_coordinates = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(i, j):
            visited.add((i, j))
            queue = collections.deque()
            
            queue.append((i, j))

            while queue:
                x, y = queue.popleft()

                for a, b in neighbour_coordinates:
                    if a + x in range(row) and b + y in range(col) and grid[a + x][b + y] == "1" and (a + x, b + y) not in visited:
                        visited.add((a + x, b + y))
                        queue.append((a +x, b + y))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1

        return islands

        

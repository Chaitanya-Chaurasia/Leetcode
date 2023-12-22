class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        max_area = 0
        row, col = len(grid), len(grid[0])
        visited = set()
        neighbour_coordinates = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def area(i, j) -> int:

            visited.add((i, j))
            queue = collections.deque()
            queue.append((i, j))
            area = 0
            while queue:
                x, y = queue.popleft()
                for a, b in neighbour_coordinates:
                    if x + a in range(row) and y + b in range(col) and grid[x + a][y + b] == 1 and (x + a, y + b) not in visited:
                        visited.add((x + a,  y + b))
                        queue.append((x + a,  y + b))
                        area += 1

            return area
        
        for i in range(row):
            for j in range(col):
                if (i, j) not in visited and grid[i][j] == 1:
                    max_area = max(max_area, area(i, j) + 1)

        return max_area
        

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # Start from the edges. Use bfs/dfs on each node until the hieght is greater than border node.
        # Do this separately for both oceans.
        # Add all the nodes with such properties to lists.
        # Finally, iterate over the sets to find common nodes.

        pacific, atlantic = set(), set()
        row, col = len (heights), len(heights[0])
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = []

        # RECURSIVE DFS
        def dfs_rec(i, j, prevHeight, visited):
            if i < 0 or j < 0 or i == row or j == col or heights[i][j] < prevHeight or (i, j) in visited:
                return

            visited.add((i, j))
            dfs(i + 1, j, heights[i][j], visited)
            dfs(i - 1, j, heights[i][j], visited)
            dfs(i, j + 1, heights[i][j], visited)
            dfs(i, j - 1, heights[i][j], visited)

        # ITERATIVE DFS
        def dfs(i, j,  visited):
            queue = collections.deque()
            queue.append((i, j))
            visited.add((i, j))

            while queue:
                curr_x, curr_y = queue.pop()
                for x, y in neighbors:
                    prevHeight = heights[curr_x][curr_y]
                    if curr_x + x in range(row) and curr_y + y in range(col) and heights[curr_x + x][curr_y + y] >= prevHeight and (curr_x + x, curr_y + y) not in visited:
                        visited.add((curr_x + x, curr_y + y))
                        queue.append((curr_x + x, curr_y + y))

        for i in range(col):
            dfs(0, i, pacific)
            dfs(row - 1, i, atlantic)
        
        for i in range(row):
            dfs(i, 0,  pacific)
            dfs(i, col - 1, atlantic)

        for i in range(row):
            for j in range(col):
                if (i, j) in atlantic and (i, j) in pacific:
                    result.append([i, j])

        return result

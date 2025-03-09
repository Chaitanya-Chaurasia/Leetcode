class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        # Check the borders for an occurence of "O". If there is, check for all of its connected nodes, and
        # change them to temporary for now.
        # Traverse the rest of the graph, and switch O for X.
        # Traverse through the borders and change T back to O.

        # We do not have to keep track of visited nodes in a different list. This is because each node
        # is marked as a "T" when visited, and we only check for nodes with "O". So they never clash.
        
        rows, cols = len(grid), len(grid[0])
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # ITERATIVE DFS
        def dfs_it(i, j):
            queue = collections.deque()
            queue.append((i, j))
            board[i][j] = "T"

            while queue:
                curr_x, curr_y = queue.pop()

                for x, y in neighbors:
                    if curr_x + x in range(row) and curr_y + y in range(col) and board[curr_x + x][curr_y + y] == "O":
                        board[curr_x + x][curr_y + y] = "T"
                        queue.append((curr_x + x, curr_y + y))

        def dfs(x, y):
            
            if x < 0 or y < 0 or x == rows or y == cols or grid[x][y] != "O":
                return
            
            grid[x][y] = "T"
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
                

        # Check the edges
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1) and grid[i][j] == "O":
                    dfs(i, j)
    
        # Traverse the graph once more and modify temps and non-temps
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "O":
                    grid[i][j] = "X"
                elif grid[i][j] == "T":
                    grid[i][j] = "O"

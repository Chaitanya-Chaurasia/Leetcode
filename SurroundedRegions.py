class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        # Check the borders for an occurence of "O". If there is, check for all of its connected nodes, and
        # change them to temporary for now.
        # Traverse the rest of the graph, and switch O for X.
        # Traverse through the borders and change T back to O.

        # We do not have to keep track of visited nodes in a different list. This is because each node
        # is marked as a "T" when visited, and we only check for nodes with "O". So they never clash.
        
        row, col = len(board), len(board[0])
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # RECURSIVE DFS
        def dfs(i, j):
            if i < 0 or j < 0 or i == row or j == col or board[i][j] != "O":
                return
            board[i][j] = "T"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1) 
        
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

        for i in range(row):
            for j in range(col):
                if (i in [0, row - 1] or j in [0, col - 1]) and board[i][j] == "O":
                    dfs_it(i, j)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"

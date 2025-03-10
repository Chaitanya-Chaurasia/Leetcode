class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        # Our approach: DFS
        # Since we need to find the topleft and bottomright coordinates, 
        # we can simply do a DFS for every group we find. 
        # Mark nodes as visited to not iterate over them again.
        # Maintain the max of row and column to return bottom-right coordinate

        rows, cols = len(land), len(land[0])
        res = []

        def dfs(x, y):
            if x < 0 or y < 0 or x == rows or y == cols or land[x][y] == 0:
                return [0, 0]
            land[x][y] = 0
            bottomRight = [x, y]

            maxRow1, maxCol1 = dfs(x + 1, y)
            maxRow2, maxCol2 = dfs(x, y + 1)

            return (max(x, maxRow1, maxRow2), max(y, maxCol1, maxCol2))

        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1:
                    bottomX, bottomY = dfs(i, j)
                    res.append([i, j, bottomX, bottomY])
        return res   

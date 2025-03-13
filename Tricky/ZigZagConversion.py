class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # Our approach: Make a grid, and start filling columns until j == numRows
        # , then iterate fill diagonals until i = 0


        # P      R
        # A    I I 
        # Y   H  N
        # P  S   G
        # A I
        # L 

        # Trick is to not actually make a 2d grid with different columns, but empty arrays. 
        # We do not care about indexing at every row, only the characters.
        # We use a variable "index" to track our movements.
        # We move down our grid until index = numRows.
        # After that, we move up until index = 0.
        # We keep doing this until all chars is s are not over.
        
        if numRows == 1 or numRows == len(s):
            return s
        grid = [[] for _ in range(numRows)]

        # initially 1 because we need to move down the grid
        row, direction = 0, 1

        for char in s:
            grid[row].append(char)
            if row == numRows - 1:
                direction = -1
            elif row == 0:
                direction = 1
            row += direction
        
        res = ""
        for i in grid:
            res += "".join(i)
        
        return res

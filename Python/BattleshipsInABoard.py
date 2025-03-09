class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        # Our approach: DFS (kind of)
        # If grid[i][j] == "X", we know it has to be a battleship.
        # The only thing we need to keep in mind is that we do not count the same battleship twice. 
        # We insert the coordinates of each unique position of battleship in a hashset
        
        rows, cols = len(board), len(board[0])
        ships = 0
        hashset = set()

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "X":
                    if ((i - 1, j) not in hashset) and ((i, j - 1) not in hashset):
                        ships += 1
                    hashset.add((i, j))
        return ships

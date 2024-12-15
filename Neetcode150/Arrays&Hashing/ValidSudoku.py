class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # duplicate rows
        for i in board:
            hashmap = defaultdict(lambda: 0)
            for j in i:
                if j != ".":
                    hashmap[j] += 1
                    if hashmap[j] > 1:
                        return False
        # duplicate columns
        hashmap = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in hashmap[j]:
                        return False
                    hashmap[j].append(board[i][j])
        # duplicate boxes
        hashmap = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    box_no = (i // 3) * 3 + (j // 3)
                    if board[i][j] in hashmap[box_no]:
                        return False
                    hashmap[box_no].append(board[i][j])
                    print(hashmap)

        return True

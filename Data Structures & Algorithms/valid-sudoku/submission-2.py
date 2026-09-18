class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9): # 0
            row_set = set()
            col_set = set()
            for j in range(9): # 0 1 2 3 4 5 6 7 8
                if board[i][j] != ".":  # 00 01 02 03 04 05 06 07 08
                    if int(board[i][j]) in col_set: 
                        return False
                    col_set.add(int(board[i][j]))
                if board[j][i] != ".": # 10 11 12 13 14 15 16 7 08
                    if int(board[j][i]) in row_set:
                        return False
                    row_set.add(int(board[j][i]))

        blocks = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

        for block_row in blocks:
            for block_col in blocks:
                block_set = set()
                for i in block_row:
                    for j in block_col:
                        if (item := board[i][j]) != ".":
                            if int(item) in block_set:
                                return False
                            block_set.add(int(item))

        return True

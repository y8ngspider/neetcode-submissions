class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Checks that each row has no duplicates
        for r in range(9):
            row = []
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in row:
                    return False
                row.append(board[r][c])
        
        #Check that each column has no dupes
        for c in range(9):
            col = []
            for r in range(9):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in col:
                    return False
                col.append(board[r][c])
        
        # Check that each box doesn't have dupes
        # columns 0-2, 3-5, 6-8
        # rows 0-2, 3-5, 6-9
        for box_r in range(3):
            for box_c in range(3):
                test = []
                r_top = box_r * 3
                r_bot = r_top + 3
                c_left = box_c * 3
                c_right = c_left + 3
                
                for r in range(r_top, r_bot):
                    for c in range(c_left, c_right):
                        if board[r][c] == ".":
                            continue
                        elif board[r][c] in test:
                            return False
                        test.append(board[r][c])
        return True

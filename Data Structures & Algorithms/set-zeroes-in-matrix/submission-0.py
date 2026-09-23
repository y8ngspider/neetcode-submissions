class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROWS, COLS = len(matrix), len(matrix[0])
        rows = set()
        cols = set()
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        rows = list(rows)
        cols = list(cols)

        for r in range(ROWS):
            for c in range(COLS):
                if c in cols or r in rows:
                    matrix[r][c] = 0

        
                
        



class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #corner, center and other

        ROWS, COLS = len(matrix), len(matrix[0])
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        
        
        

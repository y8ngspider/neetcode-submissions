class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n

        #Start from bottom row, stop at index 0
        for r in range(m-1,-1,-1):
            curRow = [0]*n
            curRow[n-1] = 1

            #Start from 2nd last column, stop at index 0
            for c in range(n-2,-1,-1):
                #Each index is the below + right
                curRow[c] = curRow[c+1] + prevRow[c]
            prevRow = curRow
        return prevRow[0]

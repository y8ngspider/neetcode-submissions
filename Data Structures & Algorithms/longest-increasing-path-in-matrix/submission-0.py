class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}
        def dfs(r,c,prev):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or matrix[r][c] <= prev:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            cur = matrix[r][c]
            up = dfs(r+1,c,cur)
            down = dfs(r-1,c,cur) 
            left = dfs(r,c-1,cur) 
            right = dfs(r,c+1,cur) 
            cache[(r,c)] = 1 + max(up,down,left,right)
            return cache[(r,c)]
        
        length = 0
        for r in range(ROWS):
            for c in range(COLS):
                length = max(length,dfs(r,c,-1))
        return length
            
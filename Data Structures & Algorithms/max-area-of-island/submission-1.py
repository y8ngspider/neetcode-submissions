class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(r, c, visited, grid):
            if c >= COLS or r >= ROWS or r < 0 or c < 0 or (r,c) in visited:
                return 0
            
            if grid[r][c] == 0:
                visited.add((r,c))
                return 0
             
            if grid[r][c] == 1:
                visited.add((r,c))
                return (1 + dfs(r+1, c, visited  , grid) 
                + dfs(r, c+1, visited,  grid)
                + dfs(r-1, c, visited,  grid)
                + dfs(r, c-1, visited,  grid))
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r,c,visited,grid))
        return maxArea


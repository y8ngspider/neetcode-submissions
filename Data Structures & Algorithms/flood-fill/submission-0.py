class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(grid: List[List[int]], r: int, c: int, same: int, color: int, visit):
            ROWS, COL = len(grid), len(grid[0])

            if (min(r,c)<0 or r == ROWS or c == COL or (r,c) in visit or grid[r][c]!=same):
                return    
            
            grid[r][c] = color
            
            visit.add((r,c))
            dfs(grid, r + 1, c, same, color, visit)  # down
            dfs(grid, r - 1, c, same, color, visit)
            dfs(grid, r, c + 1, same, color, visit)
            dfs(grid, r, c - 1, same, color, visit)
        visit = set()    
        same = image[sr][sc]
        dfs(image, sr, sc, same, color, visit)
        return image


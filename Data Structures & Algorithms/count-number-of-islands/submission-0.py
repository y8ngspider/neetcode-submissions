class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visit = set()

        # count number of paths
        def dfs(grid: List[List[str]], c: int, r:int, visit):
            ROW, COL = len(grid), len(grid[0])

            if min(c,r)<0 or c == COL or r == ROW or grid[r][c]=='0' or (c,r) in visit :
                return 0
            
            visit.add((c,r))
            dfs(grid, c+1 , r, visit)
            dfs(grid, c-1 , r, visit)
            dfs(grid, c , r +1 , visit)
            dfs(grid, c , r -1 , visit)
            return 1

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                count += dfs(grid, c, r, visit)
        
        return count

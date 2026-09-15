class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        length = 0
        neighbours = [(0,1),(1,0),(-1,0),(0,-1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    q = deque([(r,c)])

                    while q:
                        cur_r, cur_c = q.popleft()
                        grid[cur_r][cur_c] = '0'
                        for dr, dc in neighbours:
                            nr, nc = cur_r+dr, cur_c+dc
                            if ROWS > nr >=0 and COLS > nc >=0 and grid[nr][nc]=='1':
                                q.append((nr,nc))
                                grid[nr][nc] = '0'
                    length += 1
        return length



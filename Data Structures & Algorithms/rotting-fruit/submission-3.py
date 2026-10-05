class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
        
        neighbours = [(0,1),(1,0),(-1,0),(0,-1)]
        minutes = -1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                
                for dr, dc in neighbours:
                    nr, nc = r + dr, c + dc
                    if ROWS > nr >= 0 and COLS > nc >= 0 and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
            minutes+=1
        print(grid)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        
        return minutes if minutes != -1 else 0
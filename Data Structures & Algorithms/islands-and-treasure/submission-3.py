class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        visit = set()
        length = 0

        def addRoom(r, c, length):
            if r == ROWS or c == COLS or r < 0 or c < 0 or (r,c) in visit or grid[r][c]==-1 or grid[r][c]==0:
                return
            grid[r][c]=length
            visit.add((r,c))
            queue.append((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    queue.append((r,c))
                    visit.add((r,c))

        while queue:
            length += 1
            for i in range(len(queue)):
                r,c = queue.popleft()
                
                addRoom(r,c+1, length)
                addRoom(r+1,c, length)
                addRoom(r-1,c, length)
                addRoom(r,c-1, length)
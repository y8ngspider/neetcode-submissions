class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multisource bfs
        # find the rotting fruits,
        # then keep updating until no more fresh fruits
        # wait isnt it just longest path from rotting fruit

        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        visit = set()
        FRESH_FRUIT = 0
        
        def rotFruit(r,c):
            nonlocal count
            if r == ROWS or c == COLS or r < 0 or c < 0 or (r,c) in visit or grid[r][c] == 0:
                return
            count -=1
            visit.add((r,c))
            queue.append((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    FRESH_FRUIT +=1
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visit.add((r,c))
        # append all rotting fruits to the queue first
        # then we do bfs until there's no more fresh fruits that are neighbors
        minutes = 0
        count = FRESH_FRUIT

        while queue:
            temp = count
            for i in range(len(queue)):
                r,c = queue.popleft()
                rotFruit(r+1,c)
                rotFruit(r,c+1)
                rotFruit(r-1,c)
                rotFruit(r,c-1)
            if temp > count:
                minutes+=1
        return minutes if count == 0 else  -1


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Approach:
        # 1. Find valid regions that can be changed
        # Keep a list of coords of the edges ie region cannot be added
        # Store coords in a hashset
        # 2. Change the regions
        # Mark those connected to edge 'o's as safe
        # Run bfs/dfs on them to mark other safe 'o's then overwrite

        ROWS, COLS = len(board), len(board[0])
        check = []
        for i in range(ROWS):
            check.append([False]*COLS)

        visit = set()
        q = collections.deque()

        for c in range(COLS):
            q.append((0,c))
            q.append((ROWS-1,c))
        
        for r in range(ROWS):
            q.append((r,0))
            q.append((r,COLS-1))
        
        print(q)
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if (r < 0 or c < 0 or r >= ROWS or c >= COLS 
                or (r,c) in visit or board[r][c] == 'X'):
                    continue
                visit.add((r,c))

                if board[r][c]=='O':
                    check[r][c] = True
                q.append((r+1,c))
                q.append((r,c+1))
                q.append((r-1,c))
                q.append((r,c-1))
        
        for r in range(ROWS):
            for c in range(COLS):
                if not check[r][c] and board[r][c]=="O":
                    board[r][c]="X"
        print(check)
                



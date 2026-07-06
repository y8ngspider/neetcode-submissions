class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs on each node? 
        # greedy? the moment theres a bigger node then u cant
        # dfs that returns boolean
        pacific = set()
        atlantic = set()

        ROWS, COLS = len(heights), len(heights[0])
        def dfs(r,c,visit, prevHeight):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or heights[r][c]<prevHeight:
                return
            visit.add((r,c))
            newprevHeight = heights[r][c]
            dfs(r+1,c,visit,newprevHeight)
            dfs(r-1,c,visit,newprevHeight)
            dfs(r,c+1,visit,newprevHeight)
            dfs(r,c-1,visit,newprevHeight)
        
        for c in range(COLS):
            dfs(0,c,pacific,heights[0][c])
        
        for r in range(ROWS):
            dfs(r,0,pacific,heights[r][0])
        
        for c in range(COLS):
            dfs(ROWS-1,c,atlantic,heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])
        
        res=[]
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atlantic and (r,c) in pacific:
                    res.append(list((r,c)))
        return res


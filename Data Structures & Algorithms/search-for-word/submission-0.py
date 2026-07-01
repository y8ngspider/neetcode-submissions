class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

    
        def dfs(r,c,i):
            if len(word) == i:
                return True
            if r < 0 or c < 0 or r>=len(board) or c>= len(board[0]):
                return False
            if word[i] != board[r][c]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'
            i+=1
            
            found = (dfs(r+1, c, i) or
            dfs(r-1, c, i) or dfs(r,c+1,i) or dfs(r, c-1, i))

            board[r][c] = temp
            return found
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0):
                    return True

        return False 

            
        
 



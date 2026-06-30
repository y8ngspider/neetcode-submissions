class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Rules:
        # 1. you can only n of '(' as ')'
        # 2. ')' must come after '('

        # how can i backtrack?
        combs = []
        curComb = ""

        def helper(open_count, close_count, curComb, combs, n):
            if len(curComb) == 2 * n:
                combs.append(curComb)
                return
            if len(curComb) > 2 * n:
                return
            
            if open_count < n:
                helper(open_count+1, close_count, curComb+'(', combs, n)
            if close_count < open_count :
                helper(open_count, close_count+1, curComb+')', combs, n)
        
        helper(0,0, curComb, combs, n)
        return combs
            
            
            


            


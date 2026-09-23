class Solution:
    def myPow(self, x: float, n: int) -> float:
        def dfs(x,n):
            if n == 0:
                return 1
            half = dfs(x,n//2)
            if n % 2 == 0:
                return half * half
            else:
                return x * half * half
        if n < 0:
            return 1 / dfs(x,-n)
            
        return dfs(x,n)           

        

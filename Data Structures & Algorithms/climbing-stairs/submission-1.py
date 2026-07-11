class Solution:
    def climbStairs(self, n: int) -> int:
        visit = {}

        def add(n):
            if n in visit:
                return visit[n]
            if n == 1:
                return 1
            if n == 2:
                return 2
            res = add(n-1) + add(n-2)
            visit[n] = res
            return res
        
        return add(n)
        

            
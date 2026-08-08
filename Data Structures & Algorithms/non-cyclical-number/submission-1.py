class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        res=0
        while n!=1:
            
            while n!=0:
                res+= math.pow(n%10,2)
                n = n // 10
            
            
            if res in visit:
                return False
            visit.add(res)
            n = res
            res = 0

        return True

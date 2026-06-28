class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def sol(n,k):
            curComb, combs = [], []
            helper(1, curComb, combs, n, k)
            return combs
        
        def helper(i, curComb, combs, n, k):
            if len(curComb) == k:
                combs.append(curComb.copy())
                return
            if i > n:
                return
            
            # Choose to include
            curComb.append(i)
            helper(i+1, curComb, combs, n, k)
            curComb.pop()
            
            # Choose not to include
            helper(i+1, curComb, combs, n, k)

        return sol(n,k)
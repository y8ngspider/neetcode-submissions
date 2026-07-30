class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            if buying == True:
                memo[(i, buying)]= max(dfs(i + 1, False) - prices[i], dfs(i + 1, True))
            else:
                memo[(i, buying)]= max(dfs(i+2,True)+prices[i],dfs(i+1,False))
            return memo[(i, buying)]
        return dfs(0,True)

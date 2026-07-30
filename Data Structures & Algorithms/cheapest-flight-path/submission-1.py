class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")for _ in range(n)]
        prices[src] = 0

        for i in range(k+1):
            tmp = prices.copy()
            for s, d, cst in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + cst < tmp[d]:
                    tmp[d] = prices[s] + cst
            prices = tmp.copy()
        
        return prices[dst] if prices[dst] != float("inf") else -1

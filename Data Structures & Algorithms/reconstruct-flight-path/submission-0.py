from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        
        for src in graph:
            graph[src].sort()
        route = []
        def dfs(src):
            while graph[src]:
                next_airport = graph[src].pop(0)
                dfs(next_airport)
            route.append(src)
        
        dfs("JFK")
        return route[::-1]
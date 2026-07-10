import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for i in range(1,n+1):
            adj[i] = []
        
        for s, d, w in times:
            adj[s].append([d,w])
        
        visit = set()
        minheap = [[0, k]]
        t=0
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1
            for n2, w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap,[w2+w1,n2])

        return -1 if len(visit) != n else t
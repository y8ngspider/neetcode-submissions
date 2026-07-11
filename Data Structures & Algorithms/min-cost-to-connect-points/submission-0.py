import heapq
class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return False
        if self.rank[pa] > self.rank[pb]:
            self.par[pb] = pa
        elif self.rank[pb] > self.rank[pa]:
            self.par[pa] = pb
        else:
            self.par[pa] = pb
            self.rank[pb] +=1
        return True    

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minheap = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                heapq.heappush(minheap, (dist, i, j))
        unionFind = UnionFind(len(points))
        mst = 0
        cost = 0
        while mst < len(points) -1:
            d, n1, n2 = heapq.heappop(minheap)
            if not unionFind.union(n1,n2):
                continue
            mst+=1
            cost+=d
        return cost



        
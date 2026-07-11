import heapq
class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank =  {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
        
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x, a):
        px = self.find(x)
        pa = self.find(a)
        if px == pa:
            return False
        if self.rank[px] > self.rank[pa]:
            self.par[pa] = px
        elif self.rank[pa] > self.rank[px]:
            self.par[px] = pa
        else:
            self.par[px] = pa
            self.rank[pa] += 1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minheap = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                xi, yi = points[i]
                xj, yj = points[j]
                dist = abs(xi-xj) + abs(yi-yj)
                heapq.heappush(minheap, (dist, i, j))
        unionFind = UnionFind(n)
        mst_edges = 0
        cost = 0
        while mst_edges < n - 1:
            dist, p1, p2 = heapq.heappop(minheap)
            if unionFind.union(p1, p2):
                cost += int(dist)
                mst_edges += 1
        return cost
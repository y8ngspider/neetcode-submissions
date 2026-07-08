class UnionFind:
    def __init__(self,n):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self,x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self,a,b):
        pa = self.find(a)
        pb = self.find(b)

        if self.rank[pa] > self.rank[pb]:
            self.par[pb] = pa
        elif self.rank[pb] > self.rank[pa]:
            self.par[pa] = pb
        else:
            self.par[pa] = pb
            self.rank[pa]+=1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        tree = UnionFind(n)

        for a, b in edges:
            tree.union(a,b)
        
        h = set()
        for i in range(n):
            h.add(tree.find(i))
        print(tree.par)
        return len(h)

        
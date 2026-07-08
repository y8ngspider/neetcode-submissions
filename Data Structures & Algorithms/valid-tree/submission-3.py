class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    # find the parent
    def find(self, x):
        # compression optimization - set the parent to grandparent
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
        elif self.rank[pa] < self.rank[pb]:
            self.par[pa] =pb
        else:
            self.par[pa] = pb
            self.rank[pa] +=1
        return True
    
    def connected(self, a,b):
        if self.find(a)==self.find(b):
            return True
        return False

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree = UnionFind(n)
        if len(edges) != n-1:
            return False
        
        for n1, n2 in edges:
            if not tree.union(n1,n2):
                return False

        return True
         
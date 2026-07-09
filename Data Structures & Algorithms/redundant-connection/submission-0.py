class UnionFind:
    def __init__(self,n):
        self.par={}
        self.rank={}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
    
    def find(self,x):
        while x!=self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self,a,b):
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
            self.rank[pa] +=1
        return True
    

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        res = []
        tree = UnionFind(len(edges)+1)

        for edge in edges:

            if not tree.union(edge[0],edge[1]):
                res.append(edge)
        
        return res[-1]
        
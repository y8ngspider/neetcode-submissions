class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for dst, src in prerequisites:
            adj[src].append(dst)
        
        toposort=[]
        visit = set()
        path = set()
        def dfs(src, path, visit, adj):
            if src in path:
                return False
            if src in visit:
                return True
            
            path.add(src)
            for neighbor in adj[src]:
                if not dfs(neighbor,path,visit,adj):
                    return False
            toposort.append(src)
            path.remove(src)
            visit.add(src)
            return True
        
        for i in range(numCourses):
            if not dfs(i, path,visit,adj):
                return []
        toposort.reverse()
        return toposort

        
        
        

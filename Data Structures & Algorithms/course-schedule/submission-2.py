class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisites -> adjacency list
        # 2 hashsets, 1 for path and 1 for visited

        # Topo sort
        # run dfs on each node in adj list
        # Build adj list
        adj = {}
        for i in range(0, numCourses):
            adj[i] = []
        for dst, src in prerequisites:
            adj[src].append(dst)

        path = set()
        visit = set()

        # pass src node, path, visit, adj list
        def dfs(src, path, visit, adj):
            if src in path:
                return False
            if src in visit:
                return True
            
            path.add(src)
            for neighbor in adj[src]:
                if not dfs(neighbor, path, visit, adj):
                    return False
            path.remove(src)
            visit.add(src)
            return True

        for i in range(numCourses):
            if not(dfs(i, path, visit, adj)):
                return False
        return True

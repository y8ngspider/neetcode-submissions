class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for dst, src in prerequisites:
            adj[src].append(dst)
        
        visit = set()

        def dfs(i, visit):
            if i in visit:
                return False
            visit.add(i)
            for nei in adj[i]:
                if not dfs(nei,visit):
                    return False
            visit.remove(i)
            adj[i] = []
            return True
        for i in range(numCourses):
            if not dfs(i,visit):
                return False
        return True


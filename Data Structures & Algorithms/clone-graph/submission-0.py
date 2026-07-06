"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visit = {}

        def dfs(node,visit):
            if node == None:
                return 
            if node in visit:
                return visit[node]
            
            new = Node(node.val)
            visit[node] = new
            for neighbor in node.neighbors:
                new.neighbors.append(dfs(neighbor, visit))
                
            return new
        return dfs(node,visit)


        
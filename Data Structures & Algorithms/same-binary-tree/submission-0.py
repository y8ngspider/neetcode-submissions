# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        t1=[]
        t2=[]
        def dfs(node, t: list):
            if not node:
                return t.append(0)
            t.append(node.val)
            dfs(node.left, t)
            dfs(node.right, t)
        dfs(p, t1)
        dfs(q, t2)

        return True if t1==t2 else False

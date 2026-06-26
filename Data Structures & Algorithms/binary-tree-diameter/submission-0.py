# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #need longest path in left subtree + longest path in right
        self.res=0    
        def dfs(node):
            if not node:
                return 0
            
            lheight = dfs(node.left)
            rheight = dfs(node.right)
            self.res = max(self.res, lheight+rheight)
            return 1 + max(lheight, rheight)
        dfs(root)
        return self.res
        

            




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # Can use dfs to traverse tree
        # Base case: if node is a leaf (left and right are null)
        # Else: add node to path set
        # Call algo on next node, left and right
        # remove node from path set
     
        count=0
        def dfs(node, curMax):
            nonlocal count
            if node == None:
                return

            if node.val >= curMax:
                count+=1    
                print(node.val)
            if node.val > curMax:
                curMax = node.val

            dfs(node.left, curMax)
            dfs(node.right, curMax)
        
        dfs(root, root.val)
        return count




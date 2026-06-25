# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Define the cases
        # 1 if root is null and subroot not null
        # 2 if subroot is null and root is not null
        # 3 if subtree matches

        if root == None and subRoot:
            return False
        
        elif subRoot == None:
            return True
        
        elif self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif (root and not subRoot) or not (root and subRoot):
            return False
        elif root.val != subRoot.val:
            return False
        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
    
        

            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, s, t):
        if not s and t or not t and s:
            return False
        if not s and not t:
            return True
        left = self.isSameTree(s.left, t.left)
        right = self.isSameTree(s.right, t.right)

        return s.val == t.val and left and right
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return self.isSameTree(root, subRoot) or left or right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, p, q):
        if not q and not p:
            return True
        if (not q and p) or (not p and q):
            return False
        
        left = self.sameTree(p.left, q.left)
        right = self.sameTree(p.right, q.right)
        return left and right and p.val == q.val

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return self.sameTree(root, subRoot) or left or right
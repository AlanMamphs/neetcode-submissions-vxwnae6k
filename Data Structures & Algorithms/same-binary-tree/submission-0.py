# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same_root = False
        if p and q:
            same_root = p.val == q.val
        elif not p and not q:
            return True
        else:
            return False

        return same_root and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

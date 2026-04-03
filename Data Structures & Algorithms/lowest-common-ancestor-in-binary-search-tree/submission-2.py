# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return
        if root.val in (p.val, q.val):
            return root
        if root.val < min(q.val, p.val):
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > max(q.val, p.val):
            return self.lowestCommonAncestor(root.left, p, q)
        return root
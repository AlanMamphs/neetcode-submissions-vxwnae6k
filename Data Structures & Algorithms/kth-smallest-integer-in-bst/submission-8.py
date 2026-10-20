# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        idx = 0
        res = None
        def preorder(node):
            nonlocal idx
            nonlocal res
            if not node:
                return
            preorder(node.left)
            idx += 1
            if idx == k:
                res = node.val
                return
            preorder(node.right)
        preorder(root)
        return res
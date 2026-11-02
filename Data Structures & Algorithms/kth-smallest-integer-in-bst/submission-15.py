# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        idx = 0
        def inorder(node):
            nonlocal res, idx
            if not node:
                return
            inorder(node.left)
            idx += 1
            if idx == k:
                res = node.val
            inorder(node.right)
        inorder(root)
        return res
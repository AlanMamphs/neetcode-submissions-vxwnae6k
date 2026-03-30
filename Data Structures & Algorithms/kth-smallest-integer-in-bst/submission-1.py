# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthInorder(self, root: Optional[TreeNode], k: int, vals) -> int:
        if not root:
            return
        
        self.kthInorder(root.left, k, vals)
        vals.append(root.val)
        if k == len(vals):
            return
        self.kthInorder(root.right, k, vals)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []

        self.kthInorder(root, k, vals)
        return vals[k - 1]


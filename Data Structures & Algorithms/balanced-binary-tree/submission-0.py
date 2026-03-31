# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0, True
            left_h, l_is_balanced = dfs(root.left)
            right_h, r_is_balanced = dfs(root.right)
            return 1 + max(left_h, right_h), l_is_balanced and r_is_balanced and abs(left_h - right_h) <= 1
        _, is_balanced = dfs(root)
        return is_balanced

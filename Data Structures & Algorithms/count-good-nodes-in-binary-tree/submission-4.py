# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, prev_max):
            nonlocal res
            if not node:
                return
            if node.val >= prev_max:
                prev_max = node.val
                res += 1
            dfs(node.left, prev_max)
            dfs(node.right, prev_max)
        dfs(root, float('-inf'))
        return res
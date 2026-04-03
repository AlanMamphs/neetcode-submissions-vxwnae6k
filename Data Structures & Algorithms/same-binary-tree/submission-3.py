# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node, i=0, cache={}):
            if not node:
                cache[i] = None
                return cache
            cache[i] = node.val
            dfs(node.left, 2*i + 1, cache)
            dfs(node.right, 2*i + 2, cache)
            return cache
        return dfs(p, 0, {}) == dfs(q, 0, {})
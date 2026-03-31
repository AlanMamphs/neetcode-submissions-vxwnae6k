# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_value):
            res = 0
            if not node:
                return res

            if node.val >= max_value:
                res += 1
                max_value = node.val
            left = dfs(node.left, max_value)
            right = dfs(node.right, max_value)
            return res + left + right
        
        return dfs(root, root.val)
            
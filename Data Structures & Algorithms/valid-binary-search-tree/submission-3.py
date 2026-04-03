# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            left = dfs(node.left, low, node.val)
            right = dfs(node.right, node.val, high)
            return high > node.val > low and left and right
        return dfs(root, float('-inf'), float('inf'))

            
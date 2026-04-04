# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, float('-inf')
            
            left = dfs(node.left)
            right = dfs(node.right)

            max_with_children = node.val + max(left[0], 0) + max(right[0], 0)
            max_passthrough = node.val + max(left[0], right[0], 0)

            return max_passthrough, max(max_with_children, max_passthrough, left[1], right[1])
        
        return dfs(root)[1]

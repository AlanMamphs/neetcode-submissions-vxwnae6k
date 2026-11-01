# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root] if root else []
        res = []

        while stack:
            res.append(stack[-1].val)
            level = []
            for node in stack:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            stack = level
        return res

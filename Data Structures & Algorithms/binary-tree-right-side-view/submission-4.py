# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, 0)]
        res = []
        while stack:
            node, i = stack.pop()
            if not node:
                continue
            if i == len(res):
                res.append(None)
            res[i] = node.val
            stack.append((node.right, i + 1))
            stack.append((node.left, i + 1))
            
        return res
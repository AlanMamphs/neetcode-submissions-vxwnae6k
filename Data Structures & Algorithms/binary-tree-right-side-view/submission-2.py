from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if root:
            queue.append((root, 0))
        res = dict()

        while queue:
            node, index = queue.pop()
            res[index] = node.val

            if node.right:
                queue.append((node.right, index + 1))
            if node.left:
                queue.append((node.left, index + 1))
        return list(res.values())
            
                
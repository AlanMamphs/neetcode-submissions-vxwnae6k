from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0)])
        res =  []
        while queue:
            curr, level = queue.popleft()
            if len(res) == level:
                res.append([])
            res[level].append(curr.val)
            curr.left and queue.append((curr.left, level + 1))
            curr.right and queue.append((curr.right, level + 1))
        return res

            
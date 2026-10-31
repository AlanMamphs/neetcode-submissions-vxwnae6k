# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [root] if root else []

        res = []

        while stack:
            temp = []
            level = []
            for n in stack:
                level.append(n.val)
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
            res.append(level)
            stack = temp
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        stack = [(root, float('-inf'))]

        while stack:
            temp = []
            for n, mv in stack:
                if n.val >= mv:
                    mv = n.val
                    res += 1
                if n.left:
                    temp.append((n.left, mv))
                if n.right:
                    temp.append((n.right, mv))

            stack = temp
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float('-inf'), float('inf'))] if root else []
        while stack:
            temp = []

            for n, low, high in stack:
                if not (low < n.val < high):
                    return False
                if n.left:
                    temp.append((n.left, low, n.val))
                if n.right:
                    temp.append((n.right, n.val, high))
            stack = temp

        return True

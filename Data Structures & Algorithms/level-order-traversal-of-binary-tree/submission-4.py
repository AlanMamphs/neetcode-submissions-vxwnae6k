# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        stack = [root] if root else []
        while stack:
            res.append([n.val for n in stack])
            temp = []
            for n in stack:
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
            stack = temp
        return res
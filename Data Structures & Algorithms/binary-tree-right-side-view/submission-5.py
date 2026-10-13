# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root] if root else []

        while stack:
            res.append(stack[-1].val)
            level = []
            for x in stack:
                if x.left:
                    level.append(x.left)
                if x.right:
                    level.append(x.right)
            stack = level
        
        return res
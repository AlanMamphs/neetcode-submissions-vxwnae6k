# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = [root] if root else []
        depth = 0

        while level:
            temp = []
            for n in level:
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
            level = temp

            depth += 1
        
        return depth


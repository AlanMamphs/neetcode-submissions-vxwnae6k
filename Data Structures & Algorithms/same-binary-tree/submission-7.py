# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(a, b):
            if not a and not b:
                return True
            if b and not a or a and not b:
                return False
            if a.val != b.val:
                return False
            
            isleft = dfs(a.left, b.left)
            isright = dfs(a.right, b.right)
            return isleft and isright
        
        return dfs(p, q)
            
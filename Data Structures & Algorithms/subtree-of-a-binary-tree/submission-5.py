# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, a, b):
        if not a and not b:
            return True
        if a and not b or b and not a:
            return False
        
        if a.val != b.val:
            return False
        
        isleft = self.isSameTree(a.left, b.left)
        isright = self.isSameTree(a.right, b.right)
        return isleft and isright
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        while stack:
            n = stack.pop()
            if n.val == subRoot.val and self.isSameTree(n, subRoot):
                return True
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)
        return False
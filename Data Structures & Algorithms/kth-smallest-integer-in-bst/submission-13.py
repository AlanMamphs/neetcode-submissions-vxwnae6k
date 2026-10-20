# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        idx = 0
        res = root.val
        def inorder(node):
            nonlocal idx
            nonlocal res
        

            if not node or idx >= k:
                return

            inorder(node.left)
            
            if idx >= k:
                return
            
            idx += 1

            if idx == k:
                res = node.val
                return
            
            if idx < k:
                inorder(node.right)
        inorder(root)
        return res
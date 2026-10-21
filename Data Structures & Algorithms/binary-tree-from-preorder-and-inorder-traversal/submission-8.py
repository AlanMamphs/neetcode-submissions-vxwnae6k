# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = 0
        indexes = {x: idx for idx, x in enumerate(inorder)}
        def dfs(l, r):
            nonlocal idx
            if l > r:
                return
            node = TreeNode(preorder[idx])
            idx += 1
            mid = indexes[node.val]
            node.left = dfs(l, mid - 1)
            node.right = dfs(mid + 1, r)
            return node
        return dfs(0, len(inorder) - 1)

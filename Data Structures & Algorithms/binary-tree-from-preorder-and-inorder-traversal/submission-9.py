# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = 0
        inorder_idx = {x:idx for idx, x in enumerate(inorder)}
        
        def build(l, r):
            nonlocal idx
            if l > r:
                return
            node = TreeNode(preorder[idx])
            idx += 1
            mid = inorder_idx[node.val]

            node.left = build(l, mid -1)
            node.right = build(mid + 1, r)
            return node
        
        return build(0, len(inorder) - 1)


            
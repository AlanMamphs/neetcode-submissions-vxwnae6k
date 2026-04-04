# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # [1,2,3,4],
        # [2,1,3,4]

        if not preorder or not inorder:
            return
        v = preorder[0]
        m = inorder.index(v)
        node = TreeNode(v)
        node.left = self.buildTree(preorder[1:m+1], inorder[:m])
        node.right = self.buildTree(preorder[m+1:], inorder[m+1:])
        return node

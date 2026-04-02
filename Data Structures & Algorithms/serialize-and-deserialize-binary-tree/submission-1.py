# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import json

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = dict()
        def dfs(node, index=0):
            if not node:
                return 
            res[index] = node.val
            dfs(node.left, 2 * index + 1)
            dfs(node.right, 2 * index + 2)
        dfs(root)
        return json.dumps(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = {int(k): TreeNode(v) for k, v in json.loads(data).items()}
        for i, node in res.items():
            node.left = res.get(2 * i + 1)
            node.right = res.get(2 * i + 2)
        return res and res[0] or None

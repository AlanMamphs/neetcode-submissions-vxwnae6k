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
        data = {}
        def dfs(node, i):
            if not node:
                return
            data[i] = node.val
            dfs(node.left, 2*i+1)
            dfs(node.right, 2*i+2)
        dfs(root, 0)
        return json.dumps(data)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = {int(k): TreeNode(v) for k, v in json.loads(data).items()}
        for i, node in data.items():
            node.left = data.get(2*i+1)
            node.right = data.get(2*i+2)
        return data.get(0)
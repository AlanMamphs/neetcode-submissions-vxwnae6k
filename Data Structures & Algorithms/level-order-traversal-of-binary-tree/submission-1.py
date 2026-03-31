from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if root:
            queue.append((root, 0))
        res = defaultdict(list)

        while queue:
            node, index = queue.pop()
            res[index].append(node.val)
            if node.left:
                queue.appendleft((node.left, index + 1))
            if node.right:
                queue.appendleft((node.right, index + 1))
        return list(res.values())
            
                
            

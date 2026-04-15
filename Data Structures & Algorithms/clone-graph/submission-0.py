"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        store = defaultdict(lambda: Node())
        
        
        def dfs(root):
            if not root:
                return 
            if root in store:
                return store[root]

            local_r = store[root]
            local_r.val = root.val

            for n in root.neighbors:
                n = dfs(n)
                local_r.neighbors.append(n)

            return local_r
        
        return dfs(node)
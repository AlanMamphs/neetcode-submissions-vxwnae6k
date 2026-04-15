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

            copy = store[root]
            copy.val = root.val

            for n in root.neighbors:
                copy.neighbors.append(dfs(n))

            return copy
        
        return dfs(node)
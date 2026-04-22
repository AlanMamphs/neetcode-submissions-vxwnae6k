"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        store = dict()
        def dfs(node):
            if not node:
                return
            if node in store:
                return store[node]
            
            store[node] = Node(node.val)

            for nei in node.neighbors:
                store[node].neighbors.append(dfs(nei))
            return store[node]

        return dfs(node)




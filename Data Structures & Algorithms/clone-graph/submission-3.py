"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node'], visited=dict()) -> Optional['Node']:
        if not node: return
        if node in visited:
            return visited[node]
        clone = Node(node.val)
        visited[node] = clone

        for n in node.neighbors:
            clone.neighbors.append(self.cloneGraph(n, visited))
        return clone
    
    
        
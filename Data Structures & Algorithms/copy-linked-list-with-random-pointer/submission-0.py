from collections import defaultdict
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        root = head
        cache = defaultdict(lambda: None)
        dummy = prev = Node(0)
        while root:
            node = Node(root.val)
            prev.next = node
            prev = node
            cache[root] = node
            root = root.next
        root = head
        while root:
            node = cache[root]
            node.random = cache[root.random]
            root = root.next
        
        return dummy.next
            

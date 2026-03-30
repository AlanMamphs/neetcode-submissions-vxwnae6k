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
            prev.next = prev = cache[root] = Node(root.val)
            root = root.next
        root = head
        while root:
            cache[root].random = cache[root.random]
            root = root.next
        
        return dummy.next
            

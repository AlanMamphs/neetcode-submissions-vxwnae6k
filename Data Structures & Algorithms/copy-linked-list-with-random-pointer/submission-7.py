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
        store = defaultdict(lambda: Node(0))
        store[None] = None

        curr = head
        while curr:
            store[curr].val = curr.val
            store[curr].random = store[curr.random]
            store[curr].next = store[curr.next]
            curr = curr.next
        
        return store[head]
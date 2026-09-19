
class ListNode:
    def __init__(self, key=-1, val=-1, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
    
    def __repr__(self):
        return f"{self.prev and self.prev.val} <- {self.key}:{self.val} -> {self.next and self.next.val}"


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        self.last = ListNode()
        self.first = ListNode()
        self.last.next = self.first
        self.first.prev = self.last

    def unlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def append(self, node):
        prev = self.first.prev
        prev.next = node
        node.prev = prev
        node.next = self.first
        self.first.prev = node

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if not node:
            return -1
        self.unlink(node)
        self.append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.unlink(node)
            self.append(node)
            return
        
        node = ListNode(key, value)
        self.map[key] = node
        self.append(node)

        if len(self.map) > self.capacity:
            del self.map[self.last.next.key]
            self.unlink(self.last.next)




        
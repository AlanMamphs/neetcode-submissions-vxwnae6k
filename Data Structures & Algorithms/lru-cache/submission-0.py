class ListNode:
    def __init__(self, key=0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next, self.tail.prev = self.tail, self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        
        node.prev.next = node.next
        node.next.prev = node.prev
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

        return node.val


    def put(self, key: int, value: int) -> None:
        existing = self.get(key)
        if existing == -1:
            node = ListNode(key, value)
            self.cache[key] = node
            self.tail.prev.next = node
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node
            if len(self.cache) > self.capacity:
                node = self.head.next
                self.head.next = node.next
                node.next.prev = self.head
                del self.cache[node.key]
        else:
            self.tail.prev.val = value


        

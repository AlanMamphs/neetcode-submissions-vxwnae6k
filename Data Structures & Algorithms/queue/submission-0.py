class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self) -> bool:
        return self.length == 0

    def append(self, value: int) -> None:
        node = ListNode(value, None, self.tail)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1        


    def appendleft(self, value: int) -> None:
        node = ListNode(value, self.head)
        if self.length == 0:
            self.tail = node
            self.head = node
        else:
            self.head.prev = node
            self.head = node
        
        self.length += 1


    def pop(self) -> int:
        curr = self.tail
        prev = curr.prev if curr else None

        if self.length <= 1:
            self.tail = None
            self.head = None
            self.length = 0
        else:
            prev.next = None
            self.tail = prev
            self.length -= 1
        return curr.val if curr else -1

    def popleft(self) -> int:
        curr = self.head
        nxt = curr.next if curr else None


        if self.length <= 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            nxt.prev = None
            self.head = nxt
            self.length -= 1
            
        return  curr.val if curr else -1
    
        

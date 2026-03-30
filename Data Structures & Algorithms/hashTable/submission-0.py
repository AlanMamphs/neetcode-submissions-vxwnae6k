class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity

    def _hash_key(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self._hash_key(key)

        if not self.table[index]:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            head = self.table[index]
            prev = head
            while head:
                if head.key == key:
                    head.val = value
                    return
                head = head.next

            curr = Node(key, value)
            curr.next = self.table[index]
            self.table[index] = curr
            self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self._hash_key(key)
        head = self.table[index]

        if not head:
            return -1
        
        while head:
            if head.key == key:
                return head.val
            head = head.next

        return -1

    def remove(self, key: int) -> bool:
        index = self._hash_key(key)

        head = self.table[index]

        if not head:
            return False

        prev = None
        while head:
            if head.key == key:
                break
            prev, head = head, head.next

        if head:
            if prev:
                prev.next = head.next
            else:
                self.table[index] = self.table[index].next
            self.size -=1
            return True
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        new_table = [None] * self.capacity
    
        for node in self.table:
            if not node:
                continue
            
            index = self._hash_key(node.key)

            if not new_table[index]:
                new_table[index] = node
                continue
            
            curr_val = new_table[index]

            while curr_val and curr_val.next:
                curr_val = curr_val.next
            
            curr_val.next = node

        self.table = new_table



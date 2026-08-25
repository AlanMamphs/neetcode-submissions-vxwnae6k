class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        class Node:
            val = None
            next = None
            prev = None

        
        store = defaultdict(bool)

        for n in nums:
            if store[n]: continue

            node = Node()
            node.val = n
            store[n] = node
            if store[n - 1]:
                store[n - 1].next = node
                node.prev = store[n-1]
            if store[n + 1]:
                store[n + 1].prev = node
                node.next = store[n+1]
        
        res = 0
        nodes = set(x for x in store.values() if x and not store[x.val - 1])
        
        for node in nodes:
            count = 1
            prev = node.prev
            next = node.next
            while prev or next:
                if prev:
                    count += 1
                    prev = prev.prev
                if next:
                    count += 1
                    next = next.next
            res = max(res, count)
        return res




            

        
            
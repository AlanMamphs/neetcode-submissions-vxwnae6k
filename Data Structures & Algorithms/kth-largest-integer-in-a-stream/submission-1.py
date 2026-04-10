import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.store = []
        self.k = k
        heapq.heapify(self.store)
        for v in nums:
            self.add(v)

    def add(self, val: int) -> int:
        heapq.heappush(self.store, val)
        while len(self.store) > self.k:
            heapq.heappop(self.store)
        
        return self.store and self.store[0]

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.store = nums
        heapq.heapify(self.store)
        self.k = k
        self.shrink()

    def shrink(self):
        while self.k < len(self.store):
            heapq.heappop(self.store)

    def add(self, val: int) -> int:
        heapq.heappush(self.store, val)
        self.shrink()
        return self.store[0]





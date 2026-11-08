class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.data = []
        self.k = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.data, val)
        if len(self.data) > self.k:
            heapq.heappop(self.data)
        return self.data and self.data[0]

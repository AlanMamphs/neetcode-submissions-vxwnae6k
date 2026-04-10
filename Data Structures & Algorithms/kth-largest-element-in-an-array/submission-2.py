import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_h = []
        for n in nums:
            heapq.heappush(max_h, n)
            if len(max_h) > k:
                heapq.heappop(max_h)
        return max_h[0]
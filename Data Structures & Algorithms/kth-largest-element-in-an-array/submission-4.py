class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_h = []
        for n in nums:
            heapq.heappush(min_h, n)
            if len(min_h) > k:
                heapq.heappop(min_h)
        return min_h and min_h[0] or 0
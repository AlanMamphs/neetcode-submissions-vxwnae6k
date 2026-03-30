import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
        
        for key, val in counts.items():
            heapq.heappush(result, (val, key))
            if len(result) > k:
                heapq.heappop(result)
        
        return [x[1] for x in result]
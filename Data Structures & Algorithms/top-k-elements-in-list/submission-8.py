from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        
        for n in nums:
            count[n] += 1

        res = []

        for n, c in count.items():
            heapq.heappush(res, (c, n))
            if len(res) > k:
                heapq.heappop(res)            
        return [x[1] for x in res]


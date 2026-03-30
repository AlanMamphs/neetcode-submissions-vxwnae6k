from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        res = []
        for key, val in count.items():
            heapq.heappush(res, (val, key))
            if len(res) > k:
                heapq.heappop(res)
        return [x[1] for x in res]
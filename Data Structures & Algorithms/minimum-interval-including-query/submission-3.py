class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = sorted(enumerate(queries), key=lambda x: x[1])
        res = [-1] * len(queries)
        l = 0
        min_h = []
        for i, q in queries:
            while l < len(intervals) and intervals[l][0] <= q:
                heapq.heappush(min_h, (intervals[l][1] - intervals[l][0] + 1, intervals[l][1]))
                l += 1
            
            while min_h and min_h[0][1] < q:
                heapq.heappop(min_h)
            if min_h:
                res[i] = min_h[0][0]
        return res


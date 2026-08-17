class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        L = 0
        R = len(intervals) - 1

        x1, y1 = newInterval
        while L <= R:
            M = (R + L) // 2
            x2, y2 = intervals[M]
            if x2 < x1:
                L = M + 1
            else:
                R = M - 1
        intervals.insert(L, newInterval)
        
        res = []

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
        
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        last = float('-inf')
        count = 0
        print(intervals)
        for x, y in intervals:
            if x >= last:
                last = y
            else:
                last = min(y, last)
                count += 1
        return count
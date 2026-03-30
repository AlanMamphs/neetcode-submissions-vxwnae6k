from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i, t in enumerate(nums):
            while q and q[0][0] < (i + 1 - k):
                q.popleft()
            while q and q[-1][1] < t:
                q.pop()
            q.append((i, t))    
            if i + 1 >= k:
                res.append(q[0][1])
        return res



from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for r in range(len(nums)):
            while len(q) >= k or (q and q[0] < (r + 1 - k )):
                el = q.popleft()
            while q and nums[q[-1]] < nums[r]:
                el = q.pop()

            q.append(r)
            if r + 1 >= k:
                res.append(nums[q[0]])
        
        return res
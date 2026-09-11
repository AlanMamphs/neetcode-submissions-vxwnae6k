class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()

        res = []
        for r, n in enumerate(nums):
            if dq and dq[0] < r - k + 1:
                dq.popleft()
            while dq and nums[dq[-1]] < n:
                dq.pop()
            dq.append(r)
            

            if r + 1 >= k:
                res.append(nums[dq[0]])
        return res
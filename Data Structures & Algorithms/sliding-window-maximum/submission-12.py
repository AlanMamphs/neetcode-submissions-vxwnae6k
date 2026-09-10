
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        deq = deque()
        for r, n in enumerate(nums):
            if deq and deq[0] < r + 1 - k:
                deq.popleft()
            while deq and nums[deq[-1]] < n:
                deq.pop()
            deq.append(r)
            
            if k <= (r + 1):
                res.append(nums[deq[0]])
        return res
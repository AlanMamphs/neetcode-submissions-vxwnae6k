from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        q = deque()
        for r in range(len(nums)):
       
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)
            
            while q and q[0] < r - k + 1:
                q.popleft()
                    
            if r + 1 >= k:
                res.append(nums[q[0]])
        return res
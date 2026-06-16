class Solution:
    def _rob(self, nums):
        prev, curr = 0, 0
        for n in nums:
            curr, prev = max(n + prev, curr), curr
        return curr
    
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self._rob(nums[1:]), self._rob(nums[:-1]))
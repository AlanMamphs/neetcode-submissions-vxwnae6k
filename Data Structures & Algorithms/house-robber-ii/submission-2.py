class Solution:
    def _rob(self, nums):
        prev, curr = 0, 0

        for n in nums:
            curr, prev = max(prev + n, curr), curr
        return curr

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self._rob(nums[1:]), self._rob(nums[:-1]))
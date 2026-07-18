class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, best = nums[0], nums[0]
        for n in nums[1:]:
            curr = max(curr + n, n)
            best = max(best, curr)
        return best
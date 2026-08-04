class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = float('-inf')
        res = nums[0]
        for n in nums:
            curr = max(curr + n, n)
            res = max(res, curr)
        return res
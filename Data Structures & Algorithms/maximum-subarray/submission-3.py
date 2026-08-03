class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = float('-inf')
        for n in nums:
            curr = max(curr + n, n)
            res = max(res, curr)
            
        return res
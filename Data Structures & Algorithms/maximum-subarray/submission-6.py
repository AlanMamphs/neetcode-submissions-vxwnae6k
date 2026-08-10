class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, res = float('-inf'), nums[0]
        
        for n in nums:
            curr = max(n, curr + n)
            res = max(curr, res)
        return res
        



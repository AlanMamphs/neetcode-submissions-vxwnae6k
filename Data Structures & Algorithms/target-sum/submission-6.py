class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = dict()
        def dfs(i, amt):
            if (i, amt) in dp:
                return dp[(i, amt)]
            if i == len(nums):
                return amt == target
            res = dfs(i+1, amt + nums[i]) + dfs(i + 1, amt - nums[i])
            dp[(i, amt)] = res
            return res
        
        return dfs(0, 0)






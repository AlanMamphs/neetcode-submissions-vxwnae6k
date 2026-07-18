class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        def dfs(i, total):
            if (i, total) in dp:
                return dp[(i, total)]
            if i == n:
                return target == total
            
            res = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            dp[(i, total)] = res
            return res
        
        return dfs(0, 0)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n  = len(nums)
        nums = [1] + nums + [1]

        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for l in range(n, 0, -1):
            for r in range(l, n + 1):
                res = 0
                for i in range(l, r + 1):
                    burst_last = nums[l - 1] * nums[i] * nums[r + 1]
                    res = max(res, dp[l][i - 1] + burst_last + dp[i + 1][r])
                dp[l][r] = res
        
        return dp[1][n]
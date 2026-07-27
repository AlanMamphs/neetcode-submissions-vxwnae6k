class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            ndp = defaultdict(int)
            for amt, count in dp.items():
                ndp[amt - num] += count
                ndp[amt + num] += count
            dp = ndp
        return dp[target]






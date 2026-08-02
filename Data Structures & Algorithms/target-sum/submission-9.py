class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int, {0:1})

        for n in nums:
            ndp = defaultdict(int)
            for a, c in dp.items():
                ndp[a+n] += c
                ndp[a-n] += c
            dp = ndp
        return dp[target]

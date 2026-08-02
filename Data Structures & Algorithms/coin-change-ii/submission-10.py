class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = defaultdict(int, {0:1})
        for c in coins:
            ndp = defaultdict(int, {0:1})
            for a in range(1, amount + 1):
                ndp[a] = dp[a] + ndp[a - c]
            dp = ndp
        return dp[amount]
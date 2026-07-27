class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        R = len(coins)
        C = amount
        
        for r in range(R - 1, -1, -1):
            ndp = defaultdict(int)
            ndp[0] = 1
            for c in range(C + 1):
                ndp[c] = dp[c] + ndp[c - coins[r]]
            dp = ndp
        return dp[amount]

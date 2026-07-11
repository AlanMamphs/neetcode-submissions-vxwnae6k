class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for c in coins:
            for a in range(1, amount + 1):
                dp[a] += dp[a - c]
            
        print(dp)
        return dp[amount]

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for c in coins:
            newdp = defaultdict(int)
            dp[0] = 1
            for amt in range(amount + 1):
                newdp[amt] = dp[amt] + newdp[amt - c]
            dp = newdp
        return dp[amount]
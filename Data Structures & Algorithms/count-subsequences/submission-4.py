class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        R = len(s)
        C = len(t) 
        dp = [0] * (C + 1)
        dp[len(t)] = 1

        for r in range(R - 1, -1, -1):
            newdp = [0] * (C + 1)
            newdp[C] = 1
            for c in range(C - 1, -1, -1):
                newdp[c] = dp[c]
                if s[r] == t[c]:
                    newdp[c] += dp[c + 1]
            dp = newdp
        return dp[0]
        
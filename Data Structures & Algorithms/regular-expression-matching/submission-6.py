class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [False] * (len(p) + 1)
        dp[len(p)] = True
        for i in range(len(s), -1, -1):
            newdp = [False] * (len(p) + 1)
            newdp[len(p)] = i == len(s)
            for j in range(len(p) - 1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == '.')
                res = False
                if (j + 1)< len(p) and p[j+1] == '*':
                    res = newdp[j + 2] or (match and dp[j])
                elif match:
                    res = dp[j+1]
                newdp[j] = res
            dp = newdp
        return dp[0]
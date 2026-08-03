class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        R = len(s)
        C = len(p)

        dp = [[False] * (C + 1) for _ in range(R + 1)]

        for r in range(R, -1, -1):
            for c in range(C, -1, -1):
                if r == R and c == C:
                    dp[r][c] = True
                    continue
                
                match = r < R and c < C and p[c] in ('.', s[r])
                
                if (c + 1) < C and p[c + 1] == '*':
                    if dp[r][c + 2]:
                        dp[r][c] = True
                    elif match and (r < R and dp[r + 1][c]):
                        dp[r][c] = True
                elif match:
                    dp[r][c] = dp[r + 1][c + 1]
        return dp[0][0]
        
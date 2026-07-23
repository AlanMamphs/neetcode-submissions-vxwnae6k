class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        R = len(word1)
        C = len(word2)

        dp = list(range(C, -1, -1))
        print(dp)

        for r in range(R - 1, -1, -1):
            newdp = [0] * (C + 1)
            newdp[-1] = (R - r)
            for c in range(C - 1, -1, -1):
                if word1[r] == word2[c]:
                    newdp[c] = dp[c + 1]
                else:
                    newdp[c] = 1 + min(dp[c + 1], dp[c], newdp[c + 1])
            dp = newdp
        
        return dp[0]


                


                
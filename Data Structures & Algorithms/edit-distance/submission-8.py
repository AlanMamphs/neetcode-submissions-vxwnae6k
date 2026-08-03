class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 < word2:
            word1, word2 = word2, word1
        
        R = len(word1)
        C = len(word2)

        dp = list(range(C, -1, -1))
        for r in range(R - 1, -1, -1):
            ndp = [0] * (C + 1)
            ndp[C] = R - r
            for c in range(C - 1, -1, -1):
                if word1[r] == word2[c]:
                    ndp[c] = dp[c + 1]
                else:
                    delete = dp[c]
                    insert = ndp[c + 1]
                    replace = dp[c + 1]
                    ndp[c] = 1 + min(delete, insert, replace)
            dp = ndp
        
        return dp[0]

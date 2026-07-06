class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = list(range(m, -1, -1)) 
        
        for i in range(n - 1, -1, -1):
            newdp = [0] * (m + 1)
            newdp[m] = (n - i)
            for j in range(m - 1, -1, -1):
                if word1[j] == word2[i]:
                    res = dp[j+1]
                else:
                    insert = 1 + newdp[j+1]
                    delete = 1 + dp[j]
                    replace = 1 + dp[j + 1]
                    res = min(insert, delete, replace)
                newdp[j] = res
            dp = newdp
        return dp[0]




            


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = dict()
        def dfs(i, j, k):
            if (i, j, k) in cache:
                return cache[(i, j, k)]
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i + 1, j, k + 1):
                    res = True
            
            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j + 1, k + 1):
                    res = True
            cache[(i, j, k)] = res
            
            return res
        
        return dfs(0, 0, 0)
            
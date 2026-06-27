class Solution:
    def numDecodings(self, s: str) -> int:
        isvalid = lambda c: not c.startswith('0') and 0 < int(c) < 27
        cache = dict()
        def dfs(i):
            if i in cache:
                return cache[i]
            
            if i == len(s):
                return 1
            cache[i] = 0
            if isvalid(s[i]):
                cache[i] += dfs(i + 1)
            if i + 1 < len(s) and isvalid(s[i:i+2]):
                cache[i] += dfs(i + 2)
            return cache[i]

        return dfs(0)

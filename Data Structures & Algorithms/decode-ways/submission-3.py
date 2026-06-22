class Solution:
    def numDecodings(self, s: str) -> int:
        isvalid = lambda x: not x.startswith('0') and int(x) in range(1, 27)

        
        cache = defaultdict(int)

        def dfs(i):
            
            if i == len(s):
                return 1
            if cache[i]:
                return cache[i]
            l, r = 0, 0
            if i + 1 <= len(s) and isvalid(s[i:i+1]):
                
                l = dfs(i+1)
            if i + 2 <= len(s) and isvalid(s[i:i+2]):
                r = dfs(i+2)
            cache[i] = l + r
            return cache[i]

        return dfs(0)
        

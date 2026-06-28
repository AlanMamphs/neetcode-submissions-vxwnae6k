class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = defaultdict(bool)
        def dfs(i):
            if i == len(s):
                return True
            if i in cache:
                return cache[i]
            
            for w in wordDict:
                if s[i:].startswith(w) and dfs(i + len(w)):
                    cache[i] = True
            return cache[i]
        return dfs(0)
            

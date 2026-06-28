class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = defaultdict(bool)
        cache[len(s)] = True
        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if s[i:].startswith(w) and cache[i + len(w)]:
                    cache[i] = True

        return cache[0]
            

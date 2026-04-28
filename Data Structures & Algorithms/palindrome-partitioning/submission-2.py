class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalindrome(word):
            l = 0
            r = len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        res = []
        parts = []

        def dfs(i):
            if i == len(s):
                res.append(parts.copy())
                return
            for j in range(i, len(s)):
                if ispalindrome(s[i:j+1]):
                    parts.append(s[i:j+1])
                    dfs(j+1)
                    parts.pop()
        dfs(0)
        return res




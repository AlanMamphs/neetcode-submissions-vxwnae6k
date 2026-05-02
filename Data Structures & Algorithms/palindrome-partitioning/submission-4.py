class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalindrome(sub):
            l = 0
            r = len(sub) - 1
            while l < r:
                if sub[l] != sub[r]:
                    return False
                l = l + 1
                r = r - 1
            return True
        res = []
        def dfs(i, parts):
            if i >= len(s):
                res.append(parts.copy())
                return 
            for j in range(i, len(s)):
                if ispalindrome(s[i:j+1]):
                    parts.append(s[i:j+1])
                    dfs(j+1, parts)
                    parts.pop()
        dfs(0, [])
        return res





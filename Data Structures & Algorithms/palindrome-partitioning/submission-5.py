def ispalindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

class Solution:
    
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, parts):
            if i == len(s):
                res.append(parts.copy())
                return
            
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if ispalindrome(sub):
                    parts.append(sub)
                    dfs(j+1, parts)
                    parts.pop()
        dfs(0, [])
        return res

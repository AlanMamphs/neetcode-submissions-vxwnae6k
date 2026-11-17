class Solution:
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, parts):
            if i == len(s):
                res.append(parts.copy())
                return
            
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if self.isPalindrome(s, i, j):
                    parts.append(sub)
                    dfs(j + 1, parts)
                    parts.pop()
        dfs(0, [])
        return res
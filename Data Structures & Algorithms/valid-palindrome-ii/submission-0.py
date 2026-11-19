class Solution:
    def validPalindrome(self, s: str) -> bool:
        def dfs(l, r, attempt):
            if l >= r:
                return True
            if s[l] != s[r]:
                if not attempt:
                    return False
                return dfs(l + 1, r, False) or dfs(l, r - 1, False)
            return dfs(l + 1, r - 1, attempt)
        return dfs(0, len(s) - 1, True)
             
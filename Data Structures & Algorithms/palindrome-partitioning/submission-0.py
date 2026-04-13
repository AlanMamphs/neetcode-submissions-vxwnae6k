class Solution:
    def is_palindrome(self, word, l, r):
        while l < r:
            if word[l] != word[r]:
                return False
            l, r = l + 1, r - 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res

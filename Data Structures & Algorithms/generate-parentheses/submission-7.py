class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(brackets, l, r):
            if l == n == r:
                res.append(brackets)
                return
            if l < n:
                dfs(brackets + '(', l + 1, r)
            if r < l:
                dfs(brackets + ')', l, r + 1)
        dfs('', 0, 0)
        return res
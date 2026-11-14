class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(brackets, l, r):
            if l == r == n:
                res.append(brackets)
                return
            if l < n:
                dfs(brackets + '(', l + 1, r)
            if l > r:
                dfs(brackets + ')', l, r + 1)
            return
        dfs('', 0, 0)
        return res
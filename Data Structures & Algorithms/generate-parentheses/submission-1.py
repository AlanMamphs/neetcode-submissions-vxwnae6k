class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l = 0
        r = 0
        res = []
        def dfs(l, r, path):
            if l == r == n:
                res.append(path)
                return
            if l > n or r > n:
                return
            dfs(l + 1, r, path + '(')
            if l > r:
                dfs(l, r + 1, path + ')')
            
        dfs(0, 0, '')
        return res
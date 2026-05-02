class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        positive = set()
        negative = set()
        board = [['.'] * n for _ in range(n)]
        res = []
        def dfs(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r+c) in positive or (r-c) in negative:
                    continue
                board[r][c] = 'Q'
                cols.add(c)
                positive.add(r+c)
                negative.add(r-c)
                dfs(r+1)
                board[r][c] = '.'
                cols.remove(c)
                positive.remove(r+c)
                negative.remove(r-c)
        dfs(0)
        return res
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        negative = set()
        positive = set()

        res = []
        board = [["."] * n for _ in range(n)]
        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r + c) in positive or (r - c) in negative:
                    continue
                board[r][c] = 'Q'
                cols.add(c)
                negative.add(r - c)
                positive.add(r + c)
                dfs(r+1)
                cols.remove(c)
                negative.remove(r-c)
                positive.remove(r+c)
                board[r][c] = '.'
        dfs(0)
        return res
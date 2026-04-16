class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R = len(board)
        C = len(board[0])

        def dfs(r, c):
            if r not in range(R) or c not in range(C) or board[r][c] != 'O':
                return 
            board[r][c] = 'T'
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            up = dfs(r + 1, c)
            down = dfs(r - 1, c)
        
        for r in range(R):
            dfs(r, 0)
            dfs(r, C - 1)
        

        for c in range(C):
            dfs(0, c)
            dfs(R - 1, c)
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'

        

            
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R = len(board)
        C = len(board[0])
        
        def dfs(r, c):
            if r not in range(R) or c not in range(C) or board[r][c] != 'O':
                return
            
            board[r][c] = 'Y'

            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                dfs(r + dr, c + dc)
        

        for r in range(R):
            dfs(r, 0)
            dfs(r, C-1)
        

        for c in range(C):
            dfs(0, c)
            dfs(R - 1, c)

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'Y':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        
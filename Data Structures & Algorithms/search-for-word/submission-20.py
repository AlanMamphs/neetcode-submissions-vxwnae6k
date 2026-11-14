class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])

        def dfs(i, r, c):
            if i == len(word):
                return True
            if r not in range(R) or c not in range(C) or board[r][c] == '*' or board[r][c] != word[i]:
                return False
            v = board[r][c]
            board[r][c] = '*'

            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if dfs(i + 1, r + dr, c + dc):
                    return True
            board[r][c] = v
            return False

        for r in range(R):
            for c in range(C):
                if dfs(0, r, c):
                    return True
        return False
            
            
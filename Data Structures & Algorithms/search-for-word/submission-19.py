class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])

        def dfs(i, r, c):
            if r not in range(R) or c not in range(C) or board[r][c] == '*':
                return False
            v = board[r][c]
            if i + 1 == len(word) and v == word[i]:
                return True
            if word[i] != v:
                return False
            
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
            
            
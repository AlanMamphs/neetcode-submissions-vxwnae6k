class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        def dfs(r, c, path):
            if r not in range(R) or c not in range(C) or board[r][c] == '#':
                return False
            if len(path) > len(word) or not word.startswith(path):
                return False
            
            path += board[r][c]
            board[r][c] = '#'

            if word == path:
                return True
            if (
                dfs(r, c - 1, path)
                or dfs(r, c + 1, path)
                or dfs(r - 1, c, path)
                or dfs(r + 1, c, path)
            ):
                return True
            board[r][c] = path[-1]
            path = path[:-1]
            return False
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0] and dfs(r, c, ''):
                    return True
        return False


            
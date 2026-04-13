class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        def dfs(r, c, path, visited):
            if r not in range(R) or c not in range(C) or (r, c) in visited:
                return False
            if len(path) > len(word) or not word.startswith(path):
                return False
            
            path += board[r][c]
            visited.add((r, c))

            if word == path:
                return True
            if (
                dfs(r, c - 1, path, visited)
                or dfs(r, c + 1, path, visited)
                or dfs(r - 1, c, path, visited)
                or dfs(r + 1, c, path, visited)
            ):
                return True
            path = path[:-1]
            visited.remove((r, c))
            return False
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0] and dfs(r, c, '', set()):
                    return True
        return False


            
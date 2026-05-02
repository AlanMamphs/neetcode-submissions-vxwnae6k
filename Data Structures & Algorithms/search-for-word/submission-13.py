class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        
        def dfs(r, c, i):
            if r not in range(R) or c not in range(C):
                return False
            v = board[r][c]
            if v != word[i]:
                return False
            if i + 1 == len(word):
                return True
            board[r][c] = '*'
            for dr, dc in ((0,1), (0,-1), (1, 0), (-1, 0)):
                if dfs(r+dr, c+dc, i+1):
                    return True
            board[r][c] = v
            return False
        for r in range(R):
            for c in range(C):
                if dfs(r, c, 0):
                    return True
        return False






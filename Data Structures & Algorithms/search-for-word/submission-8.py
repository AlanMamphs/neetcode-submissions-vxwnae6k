class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])

        def dfs(r, c, prefix):
            if r not in range(R) or c not in range(C):
                return False
                
            if board[r][c] == '*' or not word.startswith(prefix):
                return False
            v = board[r][c]
            if word == prefix + v:
                return True
            
            board[r][c] = '*'

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):

                if dfs(r+dr, c+dc, prefix + v):
                    return True
            board[r][c] = v
            return False
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                   if dfs(r, c, ''):
                    return True
        return False 
        
            
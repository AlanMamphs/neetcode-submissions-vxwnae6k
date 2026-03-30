from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(lambda: defaultdict(set))

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == '.':
                    continue
                if v in rows[r] | cols[c] | boxes[r // 3][c // 3]:
                    return False
                rows[r].add(v)
                cols[c].add(v)
                boxes[r // 3][c // 3].add(v)
        return True
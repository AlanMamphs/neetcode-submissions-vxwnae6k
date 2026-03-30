class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        
        for i in range(9):
            seen_h = set()
            seen_v = set()
            for j in range(9):
                box = boxes[i // 3][j // 3]
                num_h = board[i][j]
                num_v = board[j][i]
                if num_h != '.':
                    if num_h in seen_h:
                        return False
                    if num_h in box:
                        return False
                    seen_h.add(num_h)
                    box.add(num_h)
                if num_v != '.':
                    if num_v in seen_v:
                        return False
                    seen_v.add(num_v)
        return True
                
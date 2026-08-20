class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R = len(matrix)
        C = len(matrix[0])
        zero_cols = set()
        zero_rows = set()

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    zero_cols.add(c)
                    zero_rows.add(r)
        

        for r in range(R):
            for c in range(C):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0

        
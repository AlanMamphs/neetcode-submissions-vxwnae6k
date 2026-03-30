class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N = len(matrix)
        M = len(matrix[0])
        l = 0
        r = N * M - 1

        while l <= r:
            m = l + (r - l) // 2

            i, j = m // M, m % M

            v = matrix[i][j]

            if v == target:
                return True
            elif v < target:
                l = m + 1
            else:
                r = m - 1
        
        return False
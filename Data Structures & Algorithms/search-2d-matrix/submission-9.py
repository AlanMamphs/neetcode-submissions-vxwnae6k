class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])
        total = R * C
        l = 0
        r = total - 1

        while l <= r:
            m = l + (r - l) // 2
            i, j = m // C, m % C

            v = matrix[i][j]

            if v == target:
                return True
            elif v < target:
                l = m + 1
            else:
                r = m - 1
        return False

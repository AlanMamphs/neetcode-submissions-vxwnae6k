class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])
        l = 0
        r = R * C - 1

        while l <= r:
            m = l + (r - l) // 2

            i, j = m // C, (m % C)
            v = matrix[i][j]
            print(m, i, j, v)

            if v == target:
                return True
            elif v < target:
                l = m + 1
            else:
                r = m - 1

        return False

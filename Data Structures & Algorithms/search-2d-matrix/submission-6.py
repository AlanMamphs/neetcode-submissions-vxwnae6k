class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])
        l = 0
        r = M * N - 1

        while l <= r:
            mid = l + (r - l) // 2

            i , j = mid // N, mid % N
            v = matrix[i][j]
            print(mid, i, j, v)
            if v == target:
                return True
            elif v < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
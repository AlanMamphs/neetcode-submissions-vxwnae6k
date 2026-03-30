class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])

        l = 0 
        r = R * C - 1

        while l <= r:
            m = l + (r - l) // 2

            i, j = m // C, m % C

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False

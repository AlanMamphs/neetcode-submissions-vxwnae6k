class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])
        N = R * C

        l = 0
        r = N - 1

        while l <= r:
            m = l + (r - l) // 2
            i = m // C
            j = m % C
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False
    
        # 0 1 2
        # 3 4 5
        # 6 7 8
            
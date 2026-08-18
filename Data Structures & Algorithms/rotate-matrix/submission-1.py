class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        def new_position(r, c, n):
            return c, n - r - 1

        for i in range(N // 2):
            for j in range(i, N - 1 - i):
                a = (i, j)
                b = new_position(*a, N)
                c = new_position(*b, N)
                d = new_position(*c, N)
                (
                    matrix[b[0]][b[1]],
                    matrix[c[0]][c[1]],
                    matrix[d[0]][d[1]],
                    matrix[a[0]][a[1]],
                ) = (
                    matrix[a[0]][a[1]],
                    matrix[b[0]][b[1]],
                    matrix[c[0]][c[1]],
                    matrix[d[0]][d[1]],
                )
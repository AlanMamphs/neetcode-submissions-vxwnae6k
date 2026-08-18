class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        def new_position(r, c, n):
            return c, n - r - 1

        for i in range((N ) // 2):
            for j in range(i, N - 1 - i):
                a = (i, j)
                b = new_position(*a, N)
                c = new_position(*b, N)
                d = new_position(*c, N)
                a_v = matrix[a[0]][a[1]]
                b_v = matrix[b[0]][b[1]]
                c_v = matrix[c[0]][c[1]]
                d_v = matrix[d[0]][d[1]]
                matrix[b[0]][b[1]] = a_v
                matrix[c[0]][c[1]] = b_v
                matrix[d[0]][d[1]] = c_v
                matrix[a[0]][a[1]] = d_v
                print(a, b, c, d)
        
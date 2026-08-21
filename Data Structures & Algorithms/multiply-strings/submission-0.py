class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        n = len(num1)
        m = len(num2)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                power = (n - i - 1) + (m - j - 1)
                res += int(num1[i]) * int(num2[j]) * (10 ** power)
        return str(res)



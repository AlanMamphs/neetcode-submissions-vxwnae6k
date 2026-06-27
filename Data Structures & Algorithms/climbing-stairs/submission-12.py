class Solution:
    def climbStairs(self, n: int) -> int:
        curr, prev = 1, 1

        for i in range(n - 1):
            curr, prev = prev + curr, curr

        return curr

    
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(31):
            bit = 1 << i
            if n & bit:
                res += 1
        return res            
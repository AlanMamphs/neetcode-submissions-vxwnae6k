class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        while n:
            bit = n & 1
            n >>= 1
            i += 1
            if bit:
                res += 1 << (32 - i)
        return res

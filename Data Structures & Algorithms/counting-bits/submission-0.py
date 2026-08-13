class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_one_bit(b):
            res = 0
            while b:
                b &= (b - 1)
                res += 1
            return res
        return [count_one_bit(b) for b in range(n + 1)]
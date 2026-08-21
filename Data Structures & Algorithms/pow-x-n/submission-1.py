class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(base, power):
            if base == 0: return 0
            if power == 0: return 1
            if power == 1: return base
            if base == 1: return 1

            res = rec(base, power // 2)
            return res * res * rec(base, power % 2)
        
        res = rec(x, abs(n))
        if n < 0:
            res = 1 / res
        return res
            
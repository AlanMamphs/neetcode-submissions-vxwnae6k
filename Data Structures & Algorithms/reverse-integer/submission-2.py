class Solution:
    def reverse(self, x: int) -> int:
        MAX_L, MAX_D = 214748364, 7
        MIN_L, MIN_D = -214748364, 8
        
        sign = x < 0 and -1 or 1
        x = abs(x)
        res = 0
        while x:
            digit = x % 10
            x //= 10
            if res > MAX_L or (res == MAX_L and digit > MAX_D):
                return 0
            if res < MIN_L or (res == MIN_L and digit > MIN_D):
                return 0
            
            res = sign * (abs(res) * 10 + digit)
        return res
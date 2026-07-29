class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        R = len(s)
        C = len(t)
        prevdp = [0] * (C + 1)
        prevdp[C] = 1
        currdp = list(prevdp)
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                res = prevdp[c]
                if s[r] == t[c]:
                    res += prevdp[c + 1]
                currdp[c] = res
            prevdp, currdp = currdp, prevdp
        return prevdp[0]
            
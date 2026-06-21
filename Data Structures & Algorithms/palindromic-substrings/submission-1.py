class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        debug = []
        for i in range(len(s)):
            for l, r in ((i, i), (i, i+1)):
                while 0 <= l and r < len(s) and s[l] == s[r]:
                    res += 1
                    debug.append(s[l:r+1])
                    l -= 1
                    r += 1
        
        return res
                
                
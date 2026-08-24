class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0
        res = []
        while r < len(s):
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            res.append(s[r+1:r+1+length])
            l = r = r + 1 + length

        return res

        
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        num_prefix = ''
        while i < len(s):
            for j in range(i, len(s)):
                if s[j] != '#':
                    num_prefix += s[j]
                else:
                    start = j + 1
                    end = start + int(num_prefix)
                    res.append(s[start:end])
                    i = end
                    num_prefix = ''
                    break
        return res
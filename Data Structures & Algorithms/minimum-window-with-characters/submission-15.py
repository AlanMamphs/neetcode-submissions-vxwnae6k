class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts_t = defaultdict(int)
        for c in t:
            counts_t[c] += 1

        l = 0
        counts_s = defaultdict(int)
        res = (-1, -1)
        have = 0
        need = len(counts_t)

        for r, c in enumerate(s):
            if c in counts_t:
                counts_s[c] += 1
                if counts_s[c] == counts_t[c]:
                    have += 1

            while have == need:
                if res == (-1, -1) or (res[1] - res[0]) > r - l:
                    res = (l, r)
                if s[l] in counts_t:
                    counts_s[s[l]] -= 1
                    if counts_s[s[l]] < counts_t[s[l]]:
                        have -= 1
                l += 1
        return '' if res == (-1, -1) else s[res[0]:res[1] + 1]


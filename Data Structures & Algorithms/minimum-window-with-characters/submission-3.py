from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = defaultdict(int)
        count_s = defaultdict(int)

        for c in t:
            count_t[c] += 1
        l = 0
        shortest = ""
        for r, c in enumerate(s):
            count_s[c] += 1
            while l <= r and all(count_s[k] >= v for k, v in count_t.items()):
                if not shortest or len(shortest) > (r - l + 1):
                    shortest = s[l:r+1]
                count_s[s[l]] -= 1
                l += 1
        return shortest

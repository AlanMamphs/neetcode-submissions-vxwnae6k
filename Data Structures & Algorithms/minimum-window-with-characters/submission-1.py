from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = defaultdict(int)

        for c in t:
            count_t[c] += 1
        
        l = 0
        count_s = defaultdict(int)
        res = ""
        for r in range(len(s)):
            count_s[s[r]] += 1
            if all(count_s[k] >= v for k, v in count_t.items()):
                print(count_s, count_t, res)
                while l < r:
                    if count_t[s[l]] < count_s[s[l]]:
                        count_s[s[l]] -= 1
                        l += 1
                    else:
                        break
                print(r, l, len(res), res and r - l + 1 < len(res) )
                if not res or r - l + 1 < len(res):
                    res = s[l:r+1]
        return res

        


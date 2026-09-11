class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = defaultdict(int)
        count_s = defaultdict(int)

        for c in t:
            count_t[c] += 1
        
        need = len(count_t)
        have = 0
        l = 0
        res = (-1, -1)
        for r, c in enumerate(s):
            count_s[c] += 1
            if c in count_t and count_t[c] == count_s[c]:
                have +=1 
            
            while have == need:
                if res == (-1, -1) or res[1] - res[0] > r - l:
                    res = (l, r)
                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        return "" if res == (-1, -1) else s[res[0]:res[1] + 1]


from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = defaultdict(int)

        for i in s:
            count_s[i] += 1
        for i in t:
            if count_s[i]:
                count_s[i] -= 1
            else:
                return False
        return sum(count_s.values()) == 0

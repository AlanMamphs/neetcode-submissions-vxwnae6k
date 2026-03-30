class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = [0] * 26
        count_s2 = [0] * 26

        for c in s1:
            count_s1[ord(c) - ord('a')] += 1

        l = 0
        for r in range(len(s2)):
            count_s2[ord(s2[r]) - ord('a')] += 1
            if r + 1 < len(s1):
                continue
            if count_s1 == count_s2:
                return True
            count_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1

        return False
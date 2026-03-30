class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = [0] * 26
        count_s2 = [0] * 26
        
        if len(s1) > len(s2):
            return False
        
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1

        l = 0

        for r in range(len(s1), len(s2)):
            if count_s1 == count_s2:
                return True
            else:
                count_s2[ord(s2[r]) - ord('a')] += 1
                count_s2[ord(s2[l]) - ord('a')] -= 1
                l += 1
        return count_s1 == count_s2
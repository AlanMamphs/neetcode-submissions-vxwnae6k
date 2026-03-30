class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        bucket_s = [0] * 26
        bucket_t = [0] * 26

        for i in range(len(s)):
            bucket_s[ord(s[i]) - ord('a')] += 1
            bucket_t[ord(t[i]) - ord('a')] += 1

        return bucket_s == bucket_t
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        bucket_s = [0] * 26
        bucket_t = [0] * 26

        for n in s:
            bucket_s[ord(n) - ord('a')] += 1

        for m in t:
            bucket_t[ord(m) - ord('a')] += 1
        
        for i in range(26):
            if bucket_s[i] != bucket_t[i]:
                return False
        return True
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_s1 = defaultdict(int)

        for c in s1:
            counts_s1[c] += 1
        
        l = 0
        counts_s2 = defaultdict(int)
        for r, c in enumerate(s2):
            counts_s2[c] += 1

            if r + 1 - l > len(s1):
                counts_s2[s2[l]] -= 1
                l += 1

            if counts_s1.items() <= counts_s2.items():
                return True
        
        return False

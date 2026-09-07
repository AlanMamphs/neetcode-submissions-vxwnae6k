class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_s1 = defaultdict(int)
        for c in s1:
            counts_s1[c] += 1
        
        counts_s2 = defaultdict(int)
        l = 0
        for i, c in enumerate(s2):
            if c not in counts_s1:
                counts_s2 = defaultdict(int)
                l = i + 1
            else:
                counts_s2[c] += 1
            while any(v > counts_s1[k] for k, v in counts_s2.items()):
                counts_s2[s2[l]] -= 1
                l += 1
            if counts_s1 == counts_s2:
                return True
        return False
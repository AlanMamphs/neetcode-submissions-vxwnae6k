from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)

        for s in strs:
            count_s = [0] * 26
            for c in s:
                count_s[ord(c) - ord('a')] += 1
            counts[tuple(count_s)].append(s)
        
        return list(counts.values())
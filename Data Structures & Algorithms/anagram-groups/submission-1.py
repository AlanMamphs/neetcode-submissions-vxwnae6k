from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - 97] += 1
            result[tuple(key)].append(s)
        return list(result.values())

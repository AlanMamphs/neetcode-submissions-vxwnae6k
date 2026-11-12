class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]

        for s in strs[1:]:
            print(s)
            j = 0
            for i in range(min(len(s), len(longest))):
                if s[i] == longest[i]:
                    j = i + 1
                    continue
                break

            longest = longest[:j]
        return longest
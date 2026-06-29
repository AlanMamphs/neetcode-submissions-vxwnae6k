class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = [0] * (len(text1) + 1)

        for i in range(len(text2) -1, -1, -1):
            newrow = [0] * (len(text1) + 1)
            for j in range(len(text1) - 1, -1, -1):
                newrow[j] = 1 + row[j+1] if text1[j] == text2[i] else max(row[j], newrow[j+1])
            row = newrow
        return row[0]

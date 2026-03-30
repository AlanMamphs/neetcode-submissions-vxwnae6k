class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        count = [0] * 26
        max_freq = 0
        l = 0
        r = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord('A')] += 1
            max_freq = max(count)

            while (r - l + 1 - max_freq) > k:
                count[ord(s[l]) - ord('A')] -= 1
                max_freq = max(count)
                l += 1
          
            longest = max(longest, r - l + 1)
        return longest
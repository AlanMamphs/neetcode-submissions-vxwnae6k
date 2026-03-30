class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        opening = '({['
        closing = ')}]'

        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            else:
                if not stack or stack.pop() != opening[closing.index(s[i])]:
                    return False

        return len(stack) == 0
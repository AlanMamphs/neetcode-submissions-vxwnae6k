class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = '([{'
        closing = {']': '[', ')': '(', '}': '{'}
        for b in s:
            if b  in opening:
                stack.append(b)
            else:
                if len(stack) and closing[b] == stack[-1]:
                        stack.pop()
                else:
                    return False
        return len(stack) == 0
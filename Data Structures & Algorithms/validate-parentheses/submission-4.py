class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingMatch = {']': '[', ')': '(', '}': '{'}
        for b in s:
            if b  in closingMatch:
                if len(stack) and closingMatch[b] == stack[-1]:
                        stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return len(stack) == 0
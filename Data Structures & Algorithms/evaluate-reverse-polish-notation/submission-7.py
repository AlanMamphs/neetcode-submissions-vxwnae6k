class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = {
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b
        }
        for t in tokens:
            if t in operators:
                right = stack.pop()
                left = stack.pop()
                stack.append(operators[t](left, right))
            else:
                stack.append(int(t))
        
        assert len(stack) == 1
        print(stack)
        return stack[0]

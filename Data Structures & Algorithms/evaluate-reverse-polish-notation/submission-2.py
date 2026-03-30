class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in '+-*/':
                right, left = stack.pop(), stack.pop()

                if t == '+':
                    res = left + right
                elif t == '-':
                    res = left - right
                elif t == '/':
                    res = int(left / right)
                else:
                    res = left * right
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[0]
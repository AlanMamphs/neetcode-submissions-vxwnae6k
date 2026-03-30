class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        nums = []
        for t in tokens:
            if t in '+-/*':
                right, left = nums.pop(), nums.pop()
                if t == '+':
                    nums.append(left + right)
                elif t == '-':
                    nums.append(left - right)
                elif t == '*':
                    nums.append(left * right)
                else:
                    nums.append(int(left / right))
            else:
                nums.append(int(t))
        return nums[0]

        # tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        # (10 / 6 / ((9 + 3) * (-11))) + 17 + 5
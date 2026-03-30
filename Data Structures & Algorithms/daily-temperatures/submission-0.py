class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                p = stack.pop()
                res[p[1]] = i - p[1]
            stack.append((t, i))
        return res
                
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                j, prev = stack.pop()
                res[j] = i - j
            stack.append((i, t))
        
        return res
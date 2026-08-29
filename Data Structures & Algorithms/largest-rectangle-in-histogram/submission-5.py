class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights)):
            h = heights[i]
            j = i
            while stack and stack[-1][1] > h:
                j, h2 = stack.pop()
                res = max(res, h2 * (i - j))
            stack.append((j, h))
        
        for i, h in stack:
            res = max(res, h * (len(heights) - i))

        return res
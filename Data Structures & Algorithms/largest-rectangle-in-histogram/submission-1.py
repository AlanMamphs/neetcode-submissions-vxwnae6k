class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # monotonic

        max_area = 0

        for i, h in enumerate(heights + [0]):
            j = i
            while stack and stack[-1][1] > h:
                j, prev = stack.pop()
                max_area = max(prev * (i - j), max_area)
            stack.append((j, h))
        return max_area
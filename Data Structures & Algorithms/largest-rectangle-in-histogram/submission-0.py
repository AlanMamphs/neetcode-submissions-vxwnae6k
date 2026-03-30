class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, n in enumerate(heights):
            j = i
            while stack and stack[-1][0] > n:
                pop = stack.pop()
                max_area = max(pop[0] * (i - pop[1]), max_area)
                j = pop[1]
            stack.append((n, j))
        
        i = len(heights)
        while stack:
            pop = stack.pop()
            max_area = max(pop[0] * (i - pop[1]), max_area)
        return max_area
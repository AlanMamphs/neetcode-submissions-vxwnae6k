class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            left = heights[l]
            right = heights[r]
            max_area = max(max_area, ((r - l) * min(left, right)))

            if left > right:
                r -= 1
            else:
                l += 1

        return max_area
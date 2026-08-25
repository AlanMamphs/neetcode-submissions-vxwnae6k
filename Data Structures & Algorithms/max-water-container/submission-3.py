class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftMax = 0
        rightMax = 0

        l = 0
        r = len(heights) - 1
        res = 0
        while l < r:
            leftMax = max(heights[l], leftMax)
            rightMax = max(heights[r], rightMax)
            if leftMax < rightMax:
                l += 1
            else:
                r -= 1
            res = max(res, min(leftMax, rightMax) * (r - l + 1))
        return res


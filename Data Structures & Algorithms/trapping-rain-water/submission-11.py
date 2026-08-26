class Solution:
    def trap(self, height: List[int]) -> int:
        right_max = defaultdict(int)

        for i in range(len(height) - 1, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        left_max = 0
        res = 0
        for i in range(len(height)):
            left_max = max(height[i], left_max)
            res += min(left_max, right_max[i]) - height[i]
        return res
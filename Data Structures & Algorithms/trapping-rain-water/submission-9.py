class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        left_max = 0
        right_max = 0
        res = 0
        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            if left_max < right_max:
                res += max(left_max - height[l], 0)
                l += 1
            else:
                res += max(right_max - height[r], 0)
                r -= 1
        return res
            
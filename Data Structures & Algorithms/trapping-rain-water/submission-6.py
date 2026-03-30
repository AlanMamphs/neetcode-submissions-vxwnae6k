class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left_max = 0
        right_max = 0

        l = 0
        r = len(height) - 1

        while l < r:
            left_max = max(height[l], left_max)
            right_max = max(height[r], right_max)
            if left_max < right_max:
                l += 1
                res += max(min(left_max, right_max) - height[l], 0)
            else:
                r -= 1
                res += max(min(left_max, right_max) - height[r], 0)


        return res
#               
#       - * * * - - * -  
#   - * - - * - - - - - -
# - - - - - - - - - - - - 
# 0 1 0 2 1 0 1 3 2 1 2 1
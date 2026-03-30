class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        l_max = 0
        r_max = 0
        res = 0
        while l < r:
            if height[l] >= l_max:
                l_max = height[l]
            if height[r] >= r_max:
                r_max = height[r]

            if height[l] <= height[r]:
                res += max(min(l_max, r_max) - height[l], 0)
                l += 1
            else:
                res += max(min(l_max, r_max) - height[r], 0)
                r -= 1
        return res

#               
#       - * * * - - * -  
#   - * - - * - - - - - -
# - - - - - - - - - - - - 
# 0 1 0 2 1 0 1 3 2 1 2 1
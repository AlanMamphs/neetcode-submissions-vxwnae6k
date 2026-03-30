class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        left_max = 0
        right_max = 0
        water = 0
        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            if left_max < right_max:
                l += 1
                water += max(left_max - height[l], 0)
                print(left_max, height[l])
            else:
                r -= 1
                water += max(right_max - height[r], 0)
        return water
    # 0,2,0,3,1,0,1,3,2,1
class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        cache = {}
        for i in range(goal, -1, -1):
            cache[i] = i
            for j in range(i, i + nums[i] + 1):
                cache[j] = i
        
        count = 0
        while goal != 0:
            goal = cache[goal]
            count += 1
        
        return count
        
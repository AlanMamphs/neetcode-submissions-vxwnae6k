class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = dict()
        goal = len(nums) -1

        for i in range(goal, -1, -1):
            cache[i] = i

            for j in range(i, i + nums[i] + 1):
                cache[j] = i
        
        count = 0

        while goal != 0:
            count += 1
            goal = cache[goal]
        
        return count

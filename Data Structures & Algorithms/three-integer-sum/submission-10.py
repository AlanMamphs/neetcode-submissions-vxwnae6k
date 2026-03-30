class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = list()
        for i, x in enumerate(nums):
            if x > 0:
                # all positive numbers remain
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -x
            l = i + 1
            r = len(nums) - 1
            while l < r:
                _sum = nums[l] + nums[r]
                if _sum < target:
                    l += 1
                elif _sum > target:
                    r -= 1
                else:
                    res.append((x, nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


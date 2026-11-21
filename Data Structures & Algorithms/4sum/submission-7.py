class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        def kSum(k, start, target):
            if k == 2:
                l = start
                r = len(nums) - 1
                while l < r:
                    _sum = nums[l] + nums[r]
                    if _sum < target:
                        l += 1
                    elif _sum > target:
                        r -= 1
                    else:
                        res.append(subset + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l > 0 and l < r and nums[l - 1] == nums[l]:
                            l += 1
            else:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    subset.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    subset.pop()
        kSum(4, 0, target)
        return res
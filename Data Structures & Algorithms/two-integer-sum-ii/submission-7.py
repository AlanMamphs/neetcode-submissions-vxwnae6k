class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
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
                        res.append(subset + [l + 1, r + 1])
                        l += 1
                        r -= 1
                        while start < l < r and nums[l] == nums[l - 1]:
                            l += 1
            else:
                for i in range(start, len(nums) - k):
                    subset.append(i + 1)
                    kSum(k - 1, i + 1, target - nums[i])
                    subset.pop()
        kSum(2, 0, target)
        return res[0]

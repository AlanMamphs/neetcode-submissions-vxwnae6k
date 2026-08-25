class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def twoSum(l, r, target):
            res = []
            while l < r:
                _sum = nums[l] + nums[r]
                if _sum == target:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                if _sum < target:
                    l += 1
                if target < _sum:
                    r -= 1
            return res

        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            two_sum = twoSum(i + 1, len(nums) - 1, -nums[i])
            if two_sum:
                for x in two_sum:
                    res.append(tuple([nums[i]] + x))
        return res
                
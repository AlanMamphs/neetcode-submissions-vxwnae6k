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
                if _sum < target:
                    l += 1
                if target < _sum:
                    r -= 1
            return res

        res = set()

        for i in range(len(nums) - 2):
            two_sum = twoSum(i + 1, len(nums) - 1, -nums[i])
            if two_sum:
                for x in two_sum:
                    res.add(tuple([nums[i]] + x))
        return list(res)
                
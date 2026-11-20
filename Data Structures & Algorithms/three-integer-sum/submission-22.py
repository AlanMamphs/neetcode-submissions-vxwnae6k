class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        def twoSum(l, r, target):
            pairs = []

            while l < r:
                _sum = nums[l] + nums[r]
                if _sum <= target:
                    if _sum == target:
                         pairs.append((nums[l], nums[r]))
                    l += 1
                else:
                    r -= 1
            return pairs
        
        res = set()

        for i in range(len(nums)):
            pairs = twoSum(i + 1, len(nums) - 1, -nums[i])
            for p in pairs:
                res.add((nums[i], *p))
        return list(res)
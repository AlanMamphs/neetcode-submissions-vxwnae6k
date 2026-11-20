class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        def twoSum(l, r, target):
            pairs = []

            while l < r:
                _sum = nums[l] + nums[r]
                if _sum < target:
                    l += 1
                elif _sum > target:
                    r -= 1
                else:
                    pairs.append((nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            return pairs
        
        res = []

        for i in range(len(nums) -2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            pairs = twoSum(i + 1, len(nums) - 1, -nums[i])
            for p in pairs:
                res.append((nums[i], *p))
        return res
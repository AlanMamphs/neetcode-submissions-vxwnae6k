class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        def twoSum(l, r, duplet_target):
            duplets = []
            while l < r:
                _sum = nums[l] + nums[r]
                if _sum < duplet_target:
                    l += 1
                elif _sum > duplet_target:
                    r -= 1
                else:
                    duplets.append((nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while l > 0 and l < r and nums[l] == nums[l - 1]:
                        l += 1
            return duplets
        
        def threeSum(start, triplet_target):
            triplets = []

            for i in range(start, len(nums)):
                a = nums[i]
                if i > start and nums[i] == nums[i - 1]:
                    continue
                pairs = twoSum(i + 1, len(nums) - 1, triplet_target - nums[i])
                for p in pairs:
                    triplets.append((a, *p))
            return triplets
        
        quadruplets = []

        for i in range(len(nums)):
            a = nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            triplets = threeSum(i + 1, target - a)
            for t in triplets:
                quadruplets.append((a, *t))
        
        return quadruplets

        



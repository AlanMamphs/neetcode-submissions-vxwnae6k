class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            if nums[i] > 0:
                break
            j = i + 1
            k = len(nums) - 1
            while j < k:
                _s = nums[i] + nums[j] + nums[k]
                if _s < 0:
                    j +=1
                elif _s > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while len(nums) > j and nums[j] == nums[j - 1]:
                        j += 1
            i += 1
            while len(nums) > i and nums[i] == nums[i - 1]:
                print("skip", i)
                i += 1
        return res
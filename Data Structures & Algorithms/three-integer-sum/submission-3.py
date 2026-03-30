class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if j == i:
                    j += 1
                    continue
                elif k == i:
                    k -= 1
                    continue
                s = nums[j] + nums[k] + nums[i]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    j += 1
        return [list(x) for x in result]
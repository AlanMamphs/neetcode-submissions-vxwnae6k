class Solution:
    def rob(self, nums: List[int]) -> int:
        two_houses_before, one_house_before = 0, 0

        for n in nums:
            curr_max = max(n + two_houses_before, one_house_before)
            two_houses_before = one_house_before
            one_house_before = curr_max
        
        return one_house_before
        
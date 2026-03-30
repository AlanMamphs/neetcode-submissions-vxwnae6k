class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while (curr := numbers[i] + numbers[j]) != target and i < j:
            if curr > target:
                j -= 1
            else:
                i += 1
        return [i + 1, j + 1]
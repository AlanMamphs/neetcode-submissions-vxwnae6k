class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        res = []
        for d in digits:
            res = [r+l for r in (res or ['']) for l in map[d]]

        return res

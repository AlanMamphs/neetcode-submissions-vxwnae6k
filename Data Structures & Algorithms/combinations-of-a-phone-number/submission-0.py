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
        def dfs(path):
            if len(path) >= len(digits):
                if path:
                    res.append(path)
                return
            i = len(path)
            for c in map[digits[i]]:
                dfs(path + c)
        dfs('')
        return res
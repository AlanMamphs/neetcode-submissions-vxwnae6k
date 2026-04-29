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
        def dfs(i, path):
            if len(path) == len(digits):
                res.append(path)
                return
            if i == len(digits):
                return
            for j in range(i, len(digits)):
                for c in map[digits[j]]:
                    dfs(j+1, path + c)
        
        if digits:
            dfs(0, '')
        return res

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R = len(matrix)
        C = len(matrix[0])
        res = []
        for i in range((min(R, C) + 1) // 2):
            left = i
            right = C - i - 1
            top = i
            bot = R - i - 1

            if top == bot and left == right:
                res.append(matrix[top][left])
                break
            
            for j in range(left, right):
                res.append(matrix[top][j])
            
            for j in range(top, bot):
                print(matrix[j][right])
                res.append(matrix[j][right])

            for j in range(right, left, -1):
                res.append(matrix[bot][j])
            
            for j in range(bot, top, -1):
                res.append(matrix[j][left])
        
                
        return res[:R*C]
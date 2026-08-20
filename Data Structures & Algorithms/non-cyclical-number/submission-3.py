class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(num):
            output = 0

            while num:
                digit = num % 10
                digit = digit ** 2
                output += digit
                num = num // 10
            return output
        
        slow = n
        fast = sum_of_squares(n)

        while slow != fast:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))
            

        return fast == 1
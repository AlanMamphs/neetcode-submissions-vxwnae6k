class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(num):
            return sum(int(d) ** 2 for d in str(num))
        
        slow = n
        fast = sum_of_squares(n)

        while slow != fast:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))
            

        return fast == 1
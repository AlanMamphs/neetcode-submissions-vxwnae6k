class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        sign_bit = 0x80000000
        result = 0
        carry = 0

        for bit in range(32):
            bit_a = (a >> bit) & 1
            bit_b = (b >> bit) & 1

            # Add the two bits and the incoming carry
            sum_bit = bit_a ^ bit_b ^ carry

            # Compute the carry for the next bit
            carry = (
                (bit_a & bit_b)
                | (carry & (bit_a ^ bit_b))
            )

            result |= sum_bit << bit

        # Interpret the 32-bit result as a signed integer.
        if result & sign_bit:
            result = ~(result ^ mask)

        return result
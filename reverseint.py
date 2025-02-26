# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes
# the value to go outside the signed 32-bit integer range [-231, 231 - 1], then
# return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Solution

# Determine the sign of the number (-1 for negative, 1 for positive).
# Convert the absolute value of x to a string and reverse it.
# Convert the reversed string back to an integer and reapply the sign.
# Check if the result is within the valid 32-bit signed integer range
# (-2^{31} to 2^{31}-1). If not, return 0.


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        rev = int(str(abs(x))[::-1]) * sign
        return rev if -(2**31) <= rev <= (2**31 - 1) else 0

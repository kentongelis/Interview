# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

# Solution

# 1. Initialize two pointers, l (left) and r (right), where l = 0 and r = x.
# 2. Use a binary search:
#   - Calculate the middle value m = l + (r - l) / 2.
#   - Check if the square of m is equal to x. If it is, return m as the square root.
#   - If the square of m is less than x, move the left pointer to m + 1, indicating the answer is in the right half.
#   - If the square of m is greater than x, move the right pointer to m - 1, indicating the answer is in the left half.
# 3. The loop continues until the left pointer exceeds the right. The value of r at this point will be the integer square root.


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            m = l + (r - l) // 2
            square = m * m
            if square == x:
                return m
            elif square < x:
                l = m + 1
            else:
                r = m - 1
        return r

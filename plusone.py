# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.


# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

# Solution

# 1. Start from the last digit of the array and move towards the first digit.
# 2. If the current digit is 9, set it to 0 because 9 + 1 results in a carry over.
# 3. If the current digit is not 9, increment it by 1 and return the array immediately, as there will be no carry over.
# 4. If all digits are processed and all were 9, prepend 1 to the array to handle the final carry over.


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Traverse the list from the last element to the first
        for i in range(len(digits) - 1, -1, -1):
            # If the current digit is 9, set it to 0
            if digits[i] == 9:
                digits[i] = 0
            else:
                # If the current digit is not 9, increment it by 1 and return the list
                digits[i] = digits[i] + 1
                return digits
        # If all digits are 9, prepend 1 to the list
        return [1] + digits

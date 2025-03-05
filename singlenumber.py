# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only
# constant extra space.


# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

# Solution

# 1. Convert the list into a set to get unique elements.
# 2. The sum of unique elements multiplied by 2 minus the sum of all elements
# gives the single number.


class Solution(object):
    def singleNumber(self, nums):
        return sum(set(nums)) * 2 - sum(nums)

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

# Solution

# 1. Iterate through the array using enumerate to get both the index and the value of each element.
# 2. Check if the current element is greater than or equal to the target:
#   -If true, return the current index as the insertion point.
# 3. If the loop completes without finding a suitable position, the target must be greater than all elements. Return the length of the array (index + 1).


class Solution:
    def searchInsert(self, nums, target):
        for index, value in enumerate(nums):
            if value >= target:
                return index
        return len(nums)

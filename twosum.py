# Given an array of integers nums and an integer target, return indices of the two numbers
# such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Solution

# 1. Initialize an empty hash map (numToIndexMap) to store the numbers we've seen so far
# and their corresponding indices.

# 2. Iterate over the array using a for loop.

# 3. For each number nums[i], calculate the difference diff between the target and the
# current number (diff = target - nums[i]).

# 4. Check if diff exists in numToIndexMap. If it does, it means we've found the two numbers that
# add up to the target. Return their indices [i, numToIndexMap.get(diff)].

# 5. If diff does not exist in the map, store the current number and its index in numToIndexMap.

# 6. If no such pair is found by the end of the loop, return null.
# (Though according to the problem constraints, a solution is guaranteed, so this case won't occur.)


class Solution:
    def twoSum(self, nums, target):
        # Create a dictionary to store numbers and their corresponding indices
        number_map = {}

        # Loop through the array
        for i, num in enumerate(nums):
            # Calculate the difference between the target and the current number
            diff = target - num

            # Check if the difference already exists in the dictionary
            if diff in number_map:
                # If it exists, return the indices of the current number and the number that adds up to the target
                return [i, number_map[diff]]

            # If it doesn't exist, add the current number and its index to the dictionary
            number_map[num] = i

        # If no two numbers add up to the target, return None
        return None

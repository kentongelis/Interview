# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Solution

# 1. Start by taking the first string in the array as the initial prefix.
# 2. Iterate over the rest of the strings in the array.
# 3. For each string, check if the current prefix is a prefix of that string.
#   - If not, reduce the prefix by removing its last character and check again.
# 4. Continue this process until you find the longest common prefix or no common prefix remains.
# 5. Return the resulting prefix.


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix) and prefix:
                prefix = prefix[:-1]
            if not prefix:
                return ""
        return prefix

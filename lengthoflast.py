# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal
# substring
#  consisting of non-space characters only.


# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

# Solution

# 1. Strip trailing whitespaces from the input string using the strip() method.
# 2. Split the string into words using the split() method.
# 3. If there are no words after stripping whitespaces, return 0.
# 4. Otherwise, return the length of the last word, which is the last element in the list of words.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()

        if not words:
            return 0

        return len(words[-1])

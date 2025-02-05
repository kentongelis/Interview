# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Solution

# 1. Create a dictionary to map closing brackets to their corresponding opening
# brackets for quick lookups: hash = {')': '(', ']': '[', '}': '{'}.
# 2. Initialize an empty stack. This will store opening brackets as they appear in the string.
# 3. Loop through each character in the string:
#   - If it’s an opening bracket ((, {, [), push it onto the stack.
#   - If it’s a closing bracket (), }, ]), check the top of the stack:
#       -If the stack is empty or the top element doesn’t match the corresponding opening
#       bracket, the string is invalid.
#       -Otherwise, pop the top element of the stack (i.e., remove the matching opening bracket).
# 4. After the loop, if the stack is not empty, it means there are unmatched opening brackets,
# so return False.
# 5. Otherwise, the string is valid, so return True.


class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack and a hash map for matching brackets
        stack = []
        hash = {")": "(", "]": "[", "}": "{"}

        # Loop through each character in the string
        for char in s:
            if char in hash:
                # If it's a closing bracket, check the stack
                if stack and stack[-1] == hash[char]:
                    stack.pop()  # Remove the matching opening bracket
                else:
                    return False  # Invalid if no match
            else:
                # Push opening brackets onto the stack
                stack.append(char)

        # Return True if stack is empty, False otherwise
        return not stack
